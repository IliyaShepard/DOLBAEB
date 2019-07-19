from service import Service


class Iqos(Service):
    def send_sms(self):
        self.session.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', json={
            'data': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': self.phone[1:],
                     'email': 'ivanov17@gmail.com', 'password': 'ivanov17',
                     'passwordConfirm': 'ivanov17'}})
