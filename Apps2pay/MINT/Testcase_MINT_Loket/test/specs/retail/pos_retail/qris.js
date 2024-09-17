const webdriver = require ('webdriverio')
const {it, describe} = require('mocha')

describe('QRIS', () => {
    it('Pembayaran QRIS berhasil', async () => {
        try {
            const btnTambahProduk = await browser.$('(//android.widget.TextView[@text="Tambah"])[1]')
            await btnTambahProduk.click()
        
            const btnCheckoutProduk = await browser.$('//android.widget.TextView[@text="CHECKOUT"]')
            await btnCheckoutProduk.click()
        
            const btnDiskonProduk = await browser.$('//android.widget.TextView[@text="Tambah diskon"]')
            await btnDiskonProduk.click()

            const btnNominalDiskonProduk = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/edInputDiscon"]')
            await btnNominalDiskonProduk.setValue('999')
            
            const btnTerapkanDiskonProduk = await browser.$('//android.widget.TextView[@text="Terapkan harga"]')
            await btnTerapkanDiskonProduk.click()
            
            const btnLanjutkan = await browser.$('//android.widget.TextView[@text="LANJUTKAN"]')
            await btnLanjutkan.click()

            const btnQris = await browser.$('(//android.widget.LinearLayout[@resource-id="com.mkpmobile.retail.mitramint:id/lnClick"])[3]')
            await btnQris.click()

            const btnBayar = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/tombolPayment"]')
            await btnBayar.click()

            const btnKonfirmasi = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/lnLanjutTr"]')
            await btnKonfirmasi.click()

            const selectApp = await browser.$('//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="NSICCS"]')
            await selectApp.click()

            const btnOK = await browser.$('[resource-id="android:id/button1"]')
            await btnOK.click()

            const btnLanjut = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/btnLanjut"]')
            await btnLanjut.click()

            const pageInputPIN = await browser.$('')
            await pageInputPIN.waitForDisplayed({timeout: 5000})

            await browser.back()
            await browser.pause(5000)
    
            const homePage = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/action_bar_root"]')
            await homePage.waitForDisplayed({timeout: 1000})

            
            console.log('Pembayaran debit berhasil')
        } catch (error) {
            console.log('Terdapat error selama pengujian yaitu :',error)
            throw error
        }
    })
})