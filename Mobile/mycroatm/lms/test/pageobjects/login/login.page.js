const path = require('path')
const loginActions = require('./actions')

class loginPage{
   constructor(){
       this.screenshotDir = path.join(__dirname, '../screenshots/login')
   }

   async login (cid, username, password) {
    await loginActions.fillForm(cid, username, password)
    await loginActions.submitLoginForm()
    await loginActions.waitForHomePage()
   }
}

module.exports = new loginPage()