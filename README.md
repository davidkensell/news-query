# Newsletter DB Query

This Python3 script queries a PostgreSQL `news` database with 3 different tables: `articles`, `authors`, and `log`.

It prints:
 * The 3 most popular articles of all time, sorted by hits
 * The most popular authors, sorted by hits
 * Days with more than 1% request error rate

## Execute the query

This program requires an active server operating PostgreSQL that can run Python3, populated with [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). One way to accomplish this locally, without provisioning remote servers through Heroku, Amazon Lightsail, or other services is to use [Vagrant](https://www.vagrantup.com/), a Linux VM.

When your DB server is up and running (see Vagrant directions below), execute the query from the terminal in the `vagrant` directory:

```bash
 $ python3 newsquery.py
```

### Download Python3

Many operating systems come with Python 2.7, but this script requires Python3.

If you haven't already, install Python3. You can find the latest release on the [Python downloads page](https://www.python.org/downloads/) or if you use homebrew run:
```
 $ brew install python
 ```

 That's not a typo. After installation, you can launch the Python 2 interpreter with `python2` and the Python 3 interpreter with `python3` from the cmd line.

### Setup a VM with Vagrant and Virtual Box

To run a local PostgreSQL server, download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to manage a virtual machine.

Download the *platform package* for your OS for VirtualBox. You don't need to launch it after install; Vagrant will do that.

For a readymade config, download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).

Enter the directory and `cd vagrant`.

### Start the VM

From terminal, run `vagrant up`. Vagrant will download and install Linux, which may take some time.

After `vagrant up` is done, run `vagrant ssh` to login to your new VM.

`cd` into `/vagrant` (which doesn't appear by `ls` command but is there nonetheless). All files in this directory are shared with the directory you started Vagrant from on your computer.

The PostgreSQL database server will automatically be started inside the VM. You can use the psql command-line tool to access it and run SQL statements.

You can log out with `ctrl-D` from the terminal, and `vagrant ssh` to log back in. If you reboot, you'll need to use `vagrant up` to restart the VM.

Rebooting can cause some problems with ssh authentication. If necessary, delete your local SHA key for Vagrant and it will add it again during boot.

## Download data

Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the `vagrant` directory, which is shared with your virtual machine.

To load the data, `cd` into the `vagrant` directory and use the command 
```
 $ psql -d news -f newsdata.sql
```

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### Troubleshooting

Running this program requires:

 * postgresql
 * Python3
 * psycopg

I ran into some challenges getting psycopg2 to work with Python3. If you're using Python3, you may need to run the following from the `/vagrant` directory:
```
pip3 install psycopg2-binary --user
```
