class historyPage {
    get buttonHistoryMenu () {
        return $ ('//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View/android.view.View[2]')
    }
    get historyPage () {
        return $('android= new UiSelector().resourceId("android:id/content")');
    }

    get buttonDari () {
        return $('//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]');
    }

    get buttonSampai () {
        return $('//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]');
    }

    get datePicker () {
        return $('android= new UiSelector().resourceId("android:id/datePicker")');
    }

    get tanggal1 () {
        return $ ('~01 September 2024')
    }
    get tanggal10 () {
        return $ ('~10 September 2024')
    }

    get buttonCancel () {
        return $ ('android= new UiSelector().resourceId("android:id/button2")');
    }

    get buttonOK () {
        return $ ('android= new UiSelector().resourceId("android:id/button2")');
    }

    get detailHistory () {
        return $('//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]');
    }

    get buttonReprintHistory () {
        return $('//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup');
    }

    async history () {
        await this.buttonHistoryMenu.click()
        await this.buttonDari.click()
        await this.tanggal1.click()
        await this.buttonOK.click()
        await this.buttonSampai.click()
        await this.tanggal10.click()
        await this.buttonOK.click()
        await this.detailHistory.click()
        await browser.pause(5000)
        await this.reprintHistory.click()
        await browser.pause(10000)
    }
}

module.exports = new historyPage()