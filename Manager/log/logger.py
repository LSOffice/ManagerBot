import datetime
max = 10

''' #experimental
def file_len():
    line_num = 0
    with open(f'./log/{datetime.date.today()}_log.txt', 'r') as f:
        for line in f:
            line = line.strip("\n")

            line_num += 1
        if line_num > max:
            open(f"./log/too-much-logs/{datetime.date.today()}_toomuch.txt", "w").writelines([l for l in open(f"./log/{datetime.date.today()}_log.txt").readlines()])
            with open(f'./log/{datetime.date.today()}_log.txt', 'a') as file:
                file.truncate(1000)
                file.close()
            f.close()
        else:
            f.close()
'''

def Log(status, user=None, guild=None, message=None, errono=0, filename=None, loc=0, activity=None, new_presence=None, cogname=None, auditaction=None, amount=None, affecteduser=None):
    now = datetime.datetime.now()
    with open(f'./log/{datetime.date.today()}_log.txt', "a") as lf:
        lf.write(now.strftime("%H:%M:%S "))
        if status == 'add':
            lf.write(f"[Discord] Guild {guild}: {user} has sent a message '{message}'\n")
        elif status == 'remove':
            lf.write(f'[Discord] Guild {guild}: {user} has deleted a message.\n')
        elif status == 'error':
            lf.write(f'[Error] {user} has set off ErroNo[{errono}]\n')
        elif status == 'bot_status':
            lf.write(f'[Bot] {message}\n')
        elif status == 'FileExistsError':
            lf.write(f'[Setup] {filename} already exists, skipping [{loc}] line of code\n')
        elif status == 'chng_pr':
            lf.write(f'[Status] Changed to {activity} {new_presence}\n')
        elif status == 'CogSuccess':
            lf.write(f'[Setup] {cogname} was loaded.\n')
        elif status == 'CogUnload':
            lf.write(f'[Setup] {cogname} was unloaded.\n')
        elif status == 'CogFail':
            lf.write(f'[Error] System has set off ErroNo[{errono}] - {cogname} failed to load.\n')
        elif status == 'audit':
            with open(f'./log/{datetime.date.today()}_auditlog.txt', "a") as f:
                if auditaction == 'clear':
                    f.write(f'[Audit] Guild {guild}: {user} used command {auditaction} for {amount} messages\n')
                    lf.write('[Audit] Action logged.\n')
                elif auditaction == 'ban':
                    f.write(f'[Audit] Guild {guild}: {user} used command {auditaction} on {affecteduser}\n')
                    lf.write('[Audit] Action logged.\n')
                elif auditaction == 'kick':
                    f.write(f'[Audit] Guild {guild}: {user} used command {auditaction} on {affecteduser}\n')
                    lf.write('[Audit] Action logged.\n')
                f.close()
        lf.close()