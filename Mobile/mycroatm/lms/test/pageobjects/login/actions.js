const { takeScreenshot } = require('../../helpers/screenshotHelper')
const loginElement = require('./elements')

class loginActions {
    async fillForm(cid, username, password) {
        await loginElement.CIDField.setValue(cid)
        await loginElement.UsernameField.setValue(username)
        await loginElement.PasswordField.setValue(password)
    }

    async submitLoginForm() {
        await loginElement.ButtonSubmit.click()
    }

    async waitForHomePage() {
        await loginElement.homePage.waitForDisplayed()
        await takeScreenshot(this.screenshotDir, 'login')
        await browser.pause(5000)   
    }
}

module.exports = new loginActions()