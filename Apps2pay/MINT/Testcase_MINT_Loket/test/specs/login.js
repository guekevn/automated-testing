const webdriverio = require ('webdriverio')
const {it, describe} = require('mocha')

describe('Login', () => {

    it('Login success', async () => {
        try {
            for (let i = 0; i < 3; i++) {
                const homePage = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/btnNext"]')
                await homePage.click()
            }
        
            const cidField = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/edCid"]')
            await cidField.setValue('00109')
        
            const usernameField = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/edUsser"]')
            await usernameField.setValue('kevintesting')
        
            const passwordField = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/edPassword"]')
            await passwordField.setValue('999999')
        
            const loginButton = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/btnLogin"]')
            await loginButton.click()
    
            const homePage = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/action_bar_root"]')
            await homePage.waitForDisplayed()
            await browser.pause(3000)

            console.log('login berhasil')
        } catch (error) {
            console.log('Terdapat error selama pengujian yaitu :', error)
            throw error
        }
    })
})



    


