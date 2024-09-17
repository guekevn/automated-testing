const webdriver = require ('webdriverio')
const {it, describe} = require('mocha')

describe('Tunai', () => {
    it('Pembayaran tunai berhasil', async () => {
        try {
            for (let i = 0; i < 3; i++) {
                const btnHide = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/showcase_button"]')
                await btnHide.click()
            }

            const menuPOS = await browser.$('//android.widget.LinearLayout[@resource-id="com.mkpmobile.retail.mitramint:id/lnProdukBiller"][1]');
            await menuPOS.click()
        
            const btnTambahProduk = await browser.$('(//android.widget.TextView[@text="Tambah"])[1]')
            await btnTambahProduk.click()
        
            const btnCheckoutProduk = await browser.$('//android.widget.TextView[@text="CHECKOUT"]')
            await btnCheckoutProduk.click()
        
            const btnLanjutkan = await browser.$('//android.widget.TextView[@text="LANJUTKAN"]')
            await btnLanjutkan.click()

            const btnTunai = await browser.$('(//android.widget.LinearLayout[@resource-id="com.mkpmobile.retail.mitramint:id/lnClick"])[1]')
            await btnTunai.click()

            const btnBayar = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/tombolPayment"]')
            await btnBayar.click()

            const btnKonfirmasi = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/lnLanjutTr"]')
            await btnKonfirmasi.click()

            const btnBayar2 = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/lnBayarTunai"]')
            await btnBayar2.click()
            await browser.pause(5000)

            const btnPrint = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/btnLanjut"]')
            await btnPrint.click()
            await browser.pause(5000)

            await browser.back()
            await browser.pause(5000)
    
            const homePage = await browser.$('[resource-id="com.mkpmobile.retail.mitramint:id/action_bar_root"]')
            await homePage.waitForDisplayed({timeout: 5000})

            
            console.log('Pembayaran tunai berhasil')
        } catch (error) {
            console.log('Terdapat error selama pengujian yaitu :',error)
            throw error
        }
    })
})