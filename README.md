#Add User to LDAP

This repository is a project that contains a program used to add users to the LDAP on the babbage server at Augsburg University.

## Contents

* Background
    * [Add New User to the Ubunutu Operating System](#Add-New-User-to-the-Ubuntu-Operating-System)
    * [Foo](#foo)


## Background - What has to be done to add a user to the LDAP?

**Note:** This is a background of what the program is doing. It is written in a way to appear these are the steps we will be taking to add a user so you can know the process. The program this repository contains DOES NOT follow these directions! The background information is for your knowledge and to help you understand what is happening behind the scenes when you run this program. 

**Also:** Prompts to enter the LDAP administrative password have been omitted in this guide. There will be times when this is needed, so be prepared to be able to answer this question.

To add a user to the LDAP, a few things must be done:
* Add new user to the ubuntu operating system
* Add the user to the LDAP
* Add a new group to the LDAP that matches the new user
* Add the user to the new group

####Add New User to the Ubuntu Operating System
First, we have to create a user on the server where the LDAP is being hosted. This is not adding a user to the LDAP, but a user of the same name to the ubuntu operating system on the server that is hosting the LDAP. We are adding this user because this LDAP is run in conjunction with a NFS mount. 

Why do we need this user on the OS in addition to the LDAP?
* We are going to use LDAP to not only authenticate login, but to grant access to a specific NFS mount. Having a specific user on the server hosting the LDAP (Babbage) enables us to restrict access inside the folders that are to be mounted. For example, one user will have access to their specific NFS folder, but not others. 


#### Add the User to the LDAP

Next, we will add the user to the LDAP. The process of adding users to the LDAP explained in this README was heavily influenced by the guide written by Karthikeyan Sadhasivam [[1]]. The explanation in this background section is an adaptation of that guide. (See footnotes for more information).

To add a user to the LDAP, we need to create a LDIF file that will hold all the information the LDAP server needs to add a user. An example of what this file looks like is contained below. 

```
dn: uid=doej,ou=users,dc=babbage,dc=augsburg,dc=edu
objectClass: posixAccount
objectClass: inetOrgPerson
objectClass: organizationalPerson
objectClass: Person
loginShell: /bin/bash
uid: doej
cn: doej
gecos: John Doe
uidNumber: 1000
gidNumber: 1000
sn: Doe
givenName: John
homeDirectory: /nfs/home/doej
```

**Notice:**
* uid and cn match
* uidNumber and gidNumber match - This is important for the NFS file access and for the LDAP grouping
* homeDirectory is /nfs/home/[uid]. This is the folder that the NFS will mount. This folder and its privileges are set by Ubuntu when you created the username in Ubuntu.

Once this file has been created, we will actually add this user to the LDAP. We will use the command below and feed it the file we created (Pretend the above file is saved as ldapUserToAdd.ldif).

``` 
ldapadd -x -W -D "cn=doej,dc=babbage,dc=augsburg,dc=edu" -f ldapUserToAdd.ldif
```


#### Add a New Group to the LDAP That Matches the New User

#### Add the User to the New Group


### ldapFilemaker

This program is used to generate 3 files the LDAP will need in order to add a user to the LDAP. 



# Footnote

[1]: https://www.thegeekstuff.com/2015/02/openldap-add-users-groups.

Sadhasivam, Karthikeyan. “How to Add LDAP Users and Groups in OpenLDAP on Linux.” The Geek Stuff, 24 Feb. 2015, www.thegeekstuff.com/2015/02/openldap-add-users-groups.
