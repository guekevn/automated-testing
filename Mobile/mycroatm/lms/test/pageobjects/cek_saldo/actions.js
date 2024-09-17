const { takeScreenshot } = require('../../helpers/screenshotHelper')
const cekSaldoElements = require('./elements')

class cekSaldoActions {
    async cekSaldoTabungan (){
        await cekSaldoElements.menuCekSaldo.click()
        await cekSaldoElements.buttonCekSaldo.click()
        await cekSaldoElements.buttonRekeningTabungan.click()
    }

    async insertCardPage (){
        await cekSaldoElements.insertCardPage.waitForDisplayed()
    }

    async inputPINPage (){
        await cekSaldoElements.inputPINPage.waitForDisplayed()
        await browser.pause(10000)
    }

    async successCekSaldoPage (){
        await cekSaldoElements.successPage.waitForDisplayed()
        await takeScreenshot(this.screenshotDir, 'cek saldo')
        await cekSaldoElements.buttonReprintCekSaldo.click()
        await browser.pause(10000)
        await cekSaldoElements.buttonSelesaiCekSaldo.click()
    }
}

module.exports = new cekSaldoActions()