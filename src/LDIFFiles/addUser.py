import subprocess
import sys
import paramiko

def main():
    pass
    # Add the user to babbage and get back uid
    # sshpass -p ${arr[4]} ssh -t -o LogLevel=QUIET administrator@141.224.38.247 "echo ${arr[4]} | sudo -S adduser --gecos '' --disabled-password ${arr[2]}" > /dev/null
    # subprocess.Popen(["sshpass", "-p", "Hex6b6e6f6c6c", "ssh", "administrator@141.224.38.247"], stdout=subprocess.PIPE)
    # process = subprocess.Popen(["hostname"], stdout=subprocess.PIPE)
    # print(process.communicate()[0])

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(
        hostname='141.224.38.247',
        username='administrator',
        password='Hex6b6e6f6c6c',
        port='22'
    )

    # session = client.get_transport().open_session()
    session = client.invoke_shell()

    session.sendall('ls -al')
    session.sendall('hostname')
    session.sendall('echo Hex6b6e6f6c6c | sudo -S shutdown -h now')

    print('done with test!')


if __name__ == "__main__":
    main()
