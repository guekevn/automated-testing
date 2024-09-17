class tarikTunaiElements {
    get menuTarikTunai() {
        return $('android= new UiSelector().text("Tarik Tunai")')
    }

    get inputNominal() {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/inputNominal")')
    }

    get buttonLanjut() {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btnLanjut")')
    }

    get buttonRekeningTabungan() {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btn_tabungan")')
    }
    get buttonRekeningGiro() {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btn_giro")')
    }

    get insertCardPage (){
        return $('android= new UiSelector().resourceId("android:id/content")')
    }

    get buttonCancelTransaction (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btl_transaksi")')
    }

    get insertPINPage (){
        return $('android= new UiSelector().resourceId("com.whty.tysecuritypin:id/keyboard_view")')
    }

    get buttonKonfirmasi (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btnKonfirmasiDetail")')
    }

    get konfirmasiPage (){
        return $('android= new UiSelector().resourceId("android:id/content")')
    }

    get buttonKonfirmasi (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btnKonfirmasiDetail")')
    }

    get successPage (){
        return $('android= new UiSelector().resourceId("android:id/content")')
    }

    get buttonReprintTarikTunai (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/linPrintStatus")')
    }

    get buttonSelesaiTarikTunai (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/linSelesaiStatus")')
    }
}

module.exports = new tarikTunaiElements()