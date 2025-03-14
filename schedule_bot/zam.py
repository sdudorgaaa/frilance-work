import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'credantials.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1HzcdvNfbqC9fga-GwRuwNqBpJl8I9W-Z7WyBitNYYco'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


#Общее наличие

def availability():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1'
    ).execute()
    val = values.get('values')[0][0]
    return val



#Первый класс наличие


def availability_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A2'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Первый класс тест


def one_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A3'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A4'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A5'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A6'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A7'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A8'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Первый класс расписание

def one_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B3'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B4'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B5'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B6'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B7'
    ).execute()
    val = values.get('values')[0][0]
    return val

def one_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B8'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Второй класс наличие


def availability_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A10'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Второй класс тест


def two_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A11'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A12'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A13'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A14'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A15'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A16'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Второй класс расписание


def two_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B11'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B12'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B13'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B14'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B15'
    ).execute()
    val = values.get('values')[0][0]
    return val

def two_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B16'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Третий класс наличие


def availability_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A18'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Третий класс тест


def three_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A19'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A20'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A21'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A22'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A23'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A24'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Третий класс расписание


def three_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B19'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B20'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B21'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B22'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B23'
    ).execute()
    val = values.get('values')[0][0]
    return val

def three_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B24'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Четвёртый класс наличие


def availability_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A26'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Четвёртый класс тест


def four_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A27'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A28'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A29'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A30'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A31'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A32'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Четвёртый класс расписание


def four_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B27'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B28'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B29'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B30'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B31'
    ).execute()
    val = values.get('values')[0][0]
    return val

def four_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B32'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Пятый класс наличие


def availability_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A34'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Пятый класс тест


def five_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A35'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A36'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A37'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A38'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A39'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A40'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_seven_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A41'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Пятый класс расписание


def five_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B35'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B36'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B37'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B38'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B39'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B40'
    ).execute()
    val = values.get('values')[0][0]
    return val

def five_seven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B41'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Шестой класс наличие


def availability_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A43'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Шестой класс тест


def six_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A44'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A45'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A46'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A47'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A48'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A49'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_seven_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A50'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Шестой класс расписание


def six_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B44'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B45'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B46'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B47'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B48'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B49'
    ).execute()
    val = values.get('values')[0][0]
    return val

def six_seven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B50'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Седьмой класс наличие


def availability_seven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A52'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Седьмой класс тест


def seven_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A53'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A54'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A55'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A56'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A57'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A58'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_seven_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A59'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Седьмой класс расписание


def seven_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B53'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B54'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B55'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B56'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B57'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B58'
    ).execute()
    val = values.get('values')[0][0]
    return val

def seven_seven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B59'
    ).execute()
    val = values.get('values')[0][0]
    return val

#Восьмой класс наличие


def availability_eight():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A61'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Восьмой класс тест


def eight_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A62'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A63'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A64'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A65'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A66'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A67'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_seven_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A68'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Восьмой класс расписание


def eight_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B62'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B63'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B64'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B65'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B66'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B67'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eight_seven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B68'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Девятый класс наличие


def availability_nine():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A70'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Девятый класс тест


def nine_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A71'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A72'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A73'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A74'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A75'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A76'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_seven_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A77'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Девятый класс расписание


def nine_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B71'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B72'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B73'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B74'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B75'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B76'
    ).execute()
    val = values.get('values')[0][0]
    return val

def nine_seven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B77'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Десятый класс наличие


def availability_ten():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A79'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Десятый класс тест


def ten_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A80'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A81'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A82'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A83'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A84'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A85'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_seven_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A86'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Десятый класс расписание


def ten_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B80'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B81'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B82'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B83'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B84'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B85'
    ).execute()
    val = values.get('values')[0][0]
    return val

def ten_seven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B86'
    ).execute()
    val = values.get('values')[0][0]
    return val

#Одинадцатый класс наличие


def availability_eleven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A88'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Одинадцатый класс тест


def eleven_one_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A89'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_two_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A90'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_three_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A91'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_four_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A92'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_five_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A93'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_six_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A94'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_seven_test():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A95'
    ).execute()
    val = values.get('values')[0][0]
    return val


#Одинадцатый класс расписание


def eleven_one():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B89'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_two():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B90'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_three():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B91'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_four():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B92'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_five():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B93'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_six():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B94'
    ).execute()
    val = values.get('values')[0][0]
    return val

def eleven_seven():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B95'
    ).execute()
    val = values.get('values')[0][0]
    return val
