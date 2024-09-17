const { takeScreenshot } = require('../../helpers/screenshotHelper')
const tarikTunaiElements = require('./elements')
class tarikTunaiActions {
    async tarikTunaiTabungan (nominal){
        await tarikTunaiElements.menuTarikTunai.click()
        await tarikTunaiElements.inputNominal.setValue(nominal)
        await tarikTunaiElements.buttonLanjut.click()
        await tarikTunaiElements.buttonRekeningTabungan.click()
    }

    async insertCardPage (){
        await tarikTunaiElements.insertCardPage.waitforDisplayed()
    }

    async inputPINPage (){
        await tarikTunaiElements.insertPINPage.waitforDisplayed()
        await browser.pause(10000)
    }

    async successTarikTunaiPage (){
        await tarikTunaiElements.successPage.waitforDisplayed()
        await takeScreenshot(screenshotDir, 'tarik tunai')
        await browser.pause(15000)
        await tarikTunaiElements.buttonReprintTarikTunai.click()
        await browser.pause(10000)
        await tarikTunaiElements.buttonSelesaiTarikTunai.click()
    }
    
}
module.exports = new tarikTunaiActions()