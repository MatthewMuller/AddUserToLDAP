
echo "-Add User-"
ldapadd -x -w Hex6b6e6f6c6c -D "cn=admin,dc=babbage,dc=augsburg,dc=edu" -f /home/administrator/LDIFFiles/ldapUserEntry.ldif;

echo "-Set User PW-"
ldappasswd -s pxe -w Hex6b6e6f6c6c -D "cn=admin,dc=babbage,dc=augsburg,dc=edu" -x "uid=pxe,ou=users,dc=babbage,dc=augsburg,dc=edu";

echo "-Add Group-"
ldapadd -x -w Hex6b6e6f6c6c -D "cn=admin,dc=babbage,dc=augsburg,dc=edu" -f /home/administrator/LDIFFiles/ldapGroupEntry.ldif;

echo "-Add User to Group-"
ldapmodify -x -w Hex6b6e6f6c6c -D "cn=admin,dc=babbage,dc=augsburg,dc=edu" -f /home/administrator/LDIFFiles/ldapAddToGroup.ldif;

echo "-Remove Files-"
echo $apw | sudo -S rm -fr /home/administrator/LDIFFiles
