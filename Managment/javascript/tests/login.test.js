var assert = require('assert');
// const { test } = require('chai/lib/chai/utils');
const {By,Key,Builder} = require("selenium-webdriver");
const { isTypedArray } = require('util/types');
require("chromedriver");
var should = require("chai").should();

//locators for login proscess
test('login', () => {
const phone_txtbox_name = "input[placeholder='טלפון']"
const send_code = "//input[@value='שלח לי קוד']"
const pass_txtbox_name = "input[placeholder='קוד']"
const login_btn = "//input[@value='כניסה']"


//test a vaild login
async function testLogin(){


let driver = await new Builder().forBrowser("chrome").build();

await driver.get("https://qa-admin.trado.co.il/#/login");

await driver.findElement(By.xpath(phone_txtbox_name)).clear
await driver.findElement(By.xpath(phone_txtbox_name)).sendKeys("1950000000")

await driver.findElement(By.xpath(send_code)).click()

await driver.findElement(By.css(pass_txtbox_name)).sendKeys("1234")

await driver.findElement(By.xpath(login_btn)).click()

let value = await driver.findElement(By.css('.loggedin_hello')).getText()

console.log(value)
assert.strictEqual(value,"שלום דניאלהתנתק")


await driver.quit();


}
})



//test invalid login when the user phone is null
test('',()=>{

async function testInvalidLogin(){


    let driver = await new Builder().forBrowser("chrome").build();
    
    await driver.get("https://qa-admin.trado.co.il/#/login");
    
    await driver.findElement(By.xpath(phone_txtbox_name)).clear
    await driver.findElement(By.xpath(phone_txtbox_name)).sendKeys("124124")
    
    let eror_massege = await driver.findElement(By.xpath("//div[contains(text(),'no such user')]")).getText()
    
    assert.strictEqual(eror_massege,"no such user")
    
    
    await driver.quit();
    
}
})



//test invalid login when the password is null

test('',()=>{

async function testLoginNoPassword(){


    let driver = await new Builder().forBrowser("chrome").build();
    
    await driver.get("https://qa-admin.trado.co.il/#/login");
    
    await driver.findElement(By.xpath(phone_txtbox_name)).clear
    await driver.findElement(By.xpath(phone_txtbox_name)).sendKeys("1950000000")
    
    await driver.findElement(By.xpath(send_code)).click()
    
    await driver.findElement(By.css(pass_txtbox_name)).sendKeys("")
    
    await driver.findElement(By.xpath(login_btn)).click()
    
    let value = await driver.findElement(By.xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[2]")).getText()
    
    console.log(value)
    assert.strictEqual(value,"faild to login")
    
    
 
    await driver.quit();

}

})









