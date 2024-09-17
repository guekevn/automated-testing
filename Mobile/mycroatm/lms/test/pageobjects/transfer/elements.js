class transferElements {
    get menuTransfer () {
        return $('android= new UiSelector().text("Transfer")')
    }

    get bankTransferList () {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/inputSelectListBank")')
    }

    get bankBRI () {
        return $('android= new UiSelector().text("BANK BRI")')
    }
    get bankBCA () {
        return $('android= new UiSelector().text("BANK BCA")')
    }
    get bankMandiri () {
        return $('android= new UiSelector().text("BANK MANDIRI")')
    }
    get bankBNI () {
        return $('android= new UiSelector().text("BANK BNI")')
    }

    get inputRekening () {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/inputRekening")')
    }

    get inputNominal () {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/inputNominal")')
    }

    get buttonLanjut () {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btnLanjut")')
    }

    get buttonRekeningTabungan () {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btn_tabungan")')
    }

    get buttonRekeningGiro () {
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

    get konfirmasiPage (){
        return $('android= new UiSelector().resourceId("android:id/content")')
    }

    get buttonKonfirmasi (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btnKonfirmasiDetail")')
    }

    get successPage (){
        return $('android= new UiSelector().resourceId("android:id/content")')
    }

    get buttonReprintTransfer (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/linPrintStatus")')
    }

    get buttonSelesaiTransfer (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/linSelesaiStatus")')
    }
}

module.exports = new transferElements()