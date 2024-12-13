import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, file_path):
    # 이메일 설정
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 이메일 본문 설정
    msg.attach(MIMEText(body, 'plain'))

    # 파일 첨부 설정
    if file_path:
        attachment = open(file_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file_path)}")
        msg.attach(part)

    # Gmail 서버 연결
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # 이메일 보내기
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("이메일 전송 성공")

    except Exception as e:
        print(f"이메일 전송 실패: {e}")

    finally:
        server.quit()
        attachment.close()

# 사용 예시
sender_email = 'kimjunhee2483@gmail.com'
sender_password = 'qsea emcp xwni hkol'
receiver_email = 'kimjunhee2483@gmail.com'
subject = '파일 첨부 테스트'
body = '이메일에 파일을 첨부했습니다.'
file_path = 'D:\Code\CoupangMaster\ShopList.xlsx'

send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, file_path)
