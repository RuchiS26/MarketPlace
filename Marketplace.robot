*** Settings *** 
Library  Selenium2Library 

*** Variables *** 
${browser}  chrome 
${url}  http://127.0.0.1:8000/ 
${Delay}  5 

*** Keywords *** 
Open Browser for Test Website
	Open Browser  ${url}  ${browser} 
	Set Selenium Speed  ${Delay} 

*** Test Cases *** 
1. Open Website Ope.
	Open Browser for Test Website

2.Enter inputs
	Input Text  id=id_username  shasha
	Input Text  id=id_password  shashank

3.Click login
	Click Element  name=login

4.Apply filters
	Click Element  name=Mobiles

5.Click on details of the product 
	Click Link  //a[contains(text(),'Details')]

6.Contact seller
	Click Link  //a[contains(text(),'Contact Seller')]

7.Go to home page
	Click Link  id=id_home

8.Click to sell product
	Click Link  //a[contains(text(),'Sell')]

9.Enter details of product
	Input Text  id=id_title  laptop
	Input Text  id=id_product  dell inspiron
	Input Text  id=id_description  this is a high performance laptop.
	Select From List By Value  xpath=//select[@id="id_tags"]  Laptops
	Input Text  id=id_price  100000
	Choose File  id=id_image  C://Users/malli/OneDrive/Desktop/d.jpg
	Click Element  id=id_post

10.Click on your ads
	Click Link  id=id_ads

11.Click on details of the product 
	Click Link  //a[contains(text(),'Details')]

12.Update product details
	Click Link  //a[contains(text(),'Update')]
	Click Element  id=id_post

13.Mark sold
	Click Link  //a[contains(text(),'Mark Sold')]
	

14.Click to sell product
	Click Link  //a[contains(text(),'Sell')]

15.Enter details of product
	Input Text  id=id_title  laptop
	Input Text  id=id_product  dell inspiron
	Input Text  id=id_description  this is a high performance laptop.
	Select From List By Value  xpath=//select[@id="id_tags"]  Laptops
	Input Text  id=id_price  100000
	Choose File  id=id_image  C://Users/malli/OneDrive/Desktop/d.jpg
	Click Element  id=id_post

16.Click on your ads
	Click Link  id=id_ads

17.Click on details of the product 
	Click Link  //a[contains(text(),'Details')]

18.Click on delete 
	Click Link  //a[contains(text(),'Delete')]
	Click Link  //a[contains(text(),'Delete')]

19.Click on Edit profile
	Click Link  //a[contains(text(),'Edit Profile')]

20.Edit profile
	Input Text  id=id_first_name  brick 
	Input Text  id=id_last_name  drink
	Choose File  id=id_image  C://Users/malli/OneDrive/Desktop/d.jpg 
	Input Text  id=id_contact  589376688
	Click Element  id=id_edit
21.Go to notifications
	Click Link  id=id_not
	Click Link  id=id_home

22.Logout 
	Click Link  //a[contains(text(),'Logout')]

23.Close browser
	Close Browser