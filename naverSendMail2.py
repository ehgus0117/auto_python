import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

# 세션 생성
s = smtplib.SMTP('smtp.naver.com', 587)

# TLS 보안 시작
s.starttls()

# 로그인 인증
s.login('fermas0372', 'dohyun941086~')

# 보낼 메세지 설정
msg = MIMEMultipart()
msg['Subject'] = '제목 : 메일 보내기 태스트'
msg['From'] = 'fermas0372@naver.com'
msg['To'] = 'kim46206758@gmail.com'
msg.attach(MIMEText('내용 : 본문 내용 테스트'))

f = r'C:\auto_python\output.csv'
fil = open(f, "rb")

part = MIMEApplication(
    fil.read(),
    Name=basename(f)
)
part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
msg.attach(part)

# 메일 보내기
s.sendmail(msg['From'], msg['To'], msg.as_string())

# 세션 종료
s.quit()