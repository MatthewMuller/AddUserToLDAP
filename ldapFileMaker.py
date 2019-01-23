import sys


##############################################################################
# This function is used to take in information about someone to add to the
# LDAP and then create the text file LDAP needs when adding a user.
##############################################################################
def ldapuserfilemaker(firstname, lastname, username, uid, gid):

    try:
        f = open("ldapUserEntry.ldif", "x")      # creates the file if needed
    except IOError:
        f = open("ldapUserEntry.ldif", "w")      # opens the file if it exist

    f.write("dn: uid=" + username + ",ou=users,dc=babbage,dc=augsburg,dc=edu" + "\n")
    f.write("objectClass: posixAccount" + "\n")
    f.write("objectClass: inetOrgPerson" + "\n")
    f.write("objectClass: organizationalPerson" + "\n")
    f.write("objectClass: Person" + "\n")
    f.write("loginShell: /bin/bash" + "\n")
    f.write("uid: " + username + "\n")
    f.write("cn: " + username + "\n")
    f.write("gecos: " + firstname + " " + lastname + "\n")
    f.write("uidNumber: " + uid + "\n")
    f.write("gidNumber: " + gid + "\n")
    f.write("sn: " + lastname + "\n")
    f.write("givenName: " + firstname + "\n")
    f.write("homeDirectory: /nfs/home/" + username)


##############################################################################
# This function is used to take in information about a group to add to the
# LDAP and then create the text file LDAP needs when adding a group.
##############################################################################
def ldapgroupfilemaker(username, gid):

    try:
        f = open("ldapGroupEntry.ldif", "x")     # creates the file if needed
    except IOError:
        f = open("ldapGroupEntry.ldif", "w")     # opens the file if it exist

    f.write("dn: cn=" + username + ",ou=groups,dc=babbage,dc=augsburg,dc=edu\n")
    f.write("objectClass: top\n")
    f.write("objectClass: posixGroup\n")
    f.write("gidNumber: " + gid)


##############################################################################
# This function is used to take in information about a group to add to the
# LDAP and then create the text file LDAP needs when adding a group.
##############################################################################
def addUserToGroup(username):

    try:
        f = open("ldapAddToGroup.ldif", "x")     # creates the file if needed
    except IOError:
        f = open("ldapAddToGroup.ldif", "w")     # opens the file if it exist

    f.write("dn: cn=" + username + ",ou=groups,dc=babbage,dc=augsburg,dc=edu\n")
    f.write("changetype: modify\n")
    f.write("add: uid\n")
    f.write("uid: " + username)


##############################################################################
# This function creates output based upon the parameters handed into the
# python script. This function is to be called when the parameters are not
# good.
##############################################################################
def badparameters():

    # The lines below build a string called args of all
    # the command line arguments
    args = ""
    for i in range(1, len(sys.argv)):
        if i + 1 == len(sys.argv):  # if its the last arg
            args += sys.argv[i]  # append only arg
        else:
            args += sys.argv[i] + ", "  # append arg and comma

    numargs = len(sys.argv) - 1

    print("INPUT ERROR\n")
    print("Received " + str(numargs) + " argument/s")
    print("Arguments - " + args)
    print("Require 6 arguments to make files for adding user/group to LDAP")


##############################################################################
# This function test the output of the ldapuserfilemaker() function. It has
# canned data and will populate the output file with it so you can see how
# the layout will look.
##############################################################################
def testldapgroupfilemaker():

    username = "doej"
    gid = "1000"
    ldapgroupfilemaker(username, gid)


##############################################################################
# This function test the output of the ldapuserfilemaker() function. It has
# canned data and will populate the output file with it so you can see how
# the layout will look.
##############################################################################
def testldapuserfilemaker():

    firstName = "John"
    lastName = "Doe"
    username = "doej"
    uid = "1000"
    gid = "1000"
    ldapuserfilemaker(firstName, lastName, username, uid, gid)


##############################################################################
# This function test the output of the addUserToGroup() function. It has
# canned data and will populate the output file with it so you can see how
# the layout will look.
##############################################################################
def testaddUserToGroup():

    username = "doej"
    addUserToGroup(username)


##############################################################################
#
##############################################################################
def main():

    #################################################
    #                     DEBUG                     #
    # Uncomment the two functions below to have     #
    # files made of the canned data in the methods  #
    # being called.                                 #
    #################################################

    # testldapuserfilemaker()     # Test the user file maker to see output
    # testldapgroupfilemaker()    # Test the group file maker to see output
    # testaddUserToGroup()        # Test the add user to group file maker

    # if the file to make is user LDIF
    if len(sys.argv) == 6:
        # sys.argv[1] - first name
        # sys.argv[2] - last name
        # sys.argv[3] - userName
        # sys.argv[4] - uid
        # sys.argv[5] - gid
        ldapuserfilemaker(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        ldapgroupfilemaker(sys.argv[1], sys.argv[5])
        addUserToGroup(sys.argv[3])
        print("ldif files have been created")
    else:
        badparameters()


main()
