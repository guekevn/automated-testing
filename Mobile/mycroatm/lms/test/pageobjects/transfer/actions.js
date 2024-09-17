const { takeScreenshot } = require('../../helpers/screenshotHelper')
const transferElements = require('./elements')
class transferActions {
    async selectTransferBRI (){
        await transferElements.menuTransfer.click()
        await transferElements.bankTransferList.click()
        await transferElements.bankBRI.click()
    }

    async inputTransferDetails (rekening, nominal) {
        await transferElements.inputRekening.setValue(rekening)
        await transferElements.inputNominal.setValue(nominal)
        await transferElements.buttonLanjut.click()
        await transferElements.buttonRekeningTabungan.click()
    }

    async waitForInsertCardPage () {
        await transferElements.insertCardPage.waitForDisplayed()
    }

    async waitForInsertPINPage () {
        await transferElements.insertPINPage.waitForDisplayed()
        await browser.pause(10000)
    }

    async waitForSuccessPage () {
        await transferElements.successPage.waitForDisplayed()
    }

    async successTransferPage () {
        await takeScreenshot(this.screenshotDir, 'transfer')
        await this.buttonReprintTransfer.click()
        await browser.pause(10000)
        await this.buttonSelesaiTransfer.click()
    }
}

module.exports = new transferActions()