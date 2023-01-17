"""In this class we have data that we have to test like data for registration_page, Login_page, Drop_down,
Profile_page & Team_page """


class Data:
    """Correct Registration"""
    Reg_Data = [{"firstname": "Ali", "lastname": "khan", "team_name": "Jon", "email": "alikhan8@mailinator.com", "password": "123456789@A"}]

    """Registration with empty Email"""
    Reg_empty_email_data = [{"firstname": "Rahul", "lastname": "shetty", "team_name": "feMale's team", "email": "", "password": "123456789@A"}]

    """Registration with wrong Email"""
    Reg_wrong_email_data = [{"firstname": "Rahul", "lastname": "shetty", "team_name": "feMale's team", "email": "hadi mailinator.com", "password": "123456"}]

    """Data to get login"""
    Login_data = [{"email": "anahita@mailinator.com", "password": "123456","wrong_email": "anahitamailinator.com", "wrong_password": "123456"}]

    """Data to manage dropdowns of phases and brackets"""
    Dropdown_Data = [{"Animal": "Cats"}]

    """Data to test the profile page"""
    Profile_Data = [{"First_Name": "Haseeb Ur", "Last_Name": "Rehman", "New_Email": "anahita1@mailinator.com"}]

    """Data to test the Team page"""
    Team_data = [{"team_name": "callback", "firstname": "laal", "lastname": "khan", "email": "pepsi2@mailinator.com", "message": "alikhan8@mailinator.com"}]