# Navigation mit der Kommandozeilec
````text
cgl044@cip1:~$ pwd
/tikhome/cgl044
cgl044@cip1:~$ ls -a
.             .bashrc  Desktop    Downloads   .gnupg    Music     .profile  Templates    .Xdefaults
..            .cache   .dmrc      .face       .local    .nv       Public    Videos       .xscreensaver
.bash_logout  .config  Documents  .face.icon  .mozilla  Pictures  .ssh      .Xauthority  .xsession-errors
cgl044@cip1:~$ mkdir Computergrundlagen
cgl044@cip1:~$ cd Computergrundlagen/
cgl044@cip1:~/Computergrundlagen$ ls / && ls /tikhome/cgl044
auto.ant       auto.web           core.1482    group       lib.usr-is-merged  proc                share    usr
auto.bee       auto.zfs           core.909205  home        libx32             root                srv      var
auto.eland     beegfs             cvmfs        home.eland  lost+found         run                 ssd      web
auto.icpopene  bin                data         lib         media              sbin                sys      work
auto.oribi     bin.usr-is-merged  dev          lib32       mnt                sbin.usr-is-merged  tikhome
auto.truenas   boot               etc          lib64       opt                scratch             tmp
Computergrundlagen  Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
cgl044@cip1:~/Computergrundlagen$ cd /etc/
cgl044@cip1:/etc$ 


````
# Arbeiten mit Dateien und Verzeichnissen

```
cgl044@cip1:~$ cd Computergrundlagen/  
cgl044@cip1:~/Computergrundlagen$ touch directory.txt  
cgl044@cip1:~/Computergrundlagen$ echo "Beistiel 123 abc" >> directory.txt    
cgl044@cip1:~/Computergrundlagen$ cat directory.txt    
Beistiel 123 abc  
cgl044@cip1:~/Computergrundlagen$ cp directory.txt directory_copy.text  
cgl044@cip1:~/Computergrundlagen$ mv directory_copy.text /tikhome/cgl044/directory.txt  
cgl044@cip1:~/Computergrundlagen$ cd ../  
cgl044@cip1:~$ rm directory.txt    
cgl044@cip1:~$ cp -R Computergrundlagen/ Computergrundlagen_copy/  
cgl044@cip1:~$ rm -r Computergrundlagen_copy/  
cgl044@cip1:~$ ls  
Computergrundlagen  Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos  
cgl044@cip1:~$
```
# Hilfe für Befehle und Pipes
`man man` ruft die man (Hilfe Page/ manual page) Page des man Befehls auf.

```
cgl044@cip1:~$ man man | wc  
man: can't resolve man7/groff_man.7  
   575    4760   34859
```
`wc` steht für word count und gibt die Zeilen, Zeichen und Bytes der man page von man aus. `|` piped die Ausgabe des `man man` Befehls in den `wc`Befehl.

```
cgl044@cip1:~$ man man | wc | wc  
man: can't resolve man7/groff_man.7  
     1       3      24

```
Gibt den `wc`der Fehlermeldung `can't resolve man7/groff_man.7` aus. Eine Zeile, drei Wörter und 24 Bytes.