pkgname=kavach-xhelp
pkgver=1
pkgrel=1
pkgdesc="Cyber Helpline App for Kavach OS"
arch=('any')
url="https://github.com/Project-K-Official/kavach-help"
license=('GPL3.0')
depends=('python3' 'python-pyqt5')
makedepends=('git')
source=("git+$url.git")
sha256sums=('SKIP')

package() {
        install -d  ${pkgdir}/usr/share/kavach-help
        install -d  ${pkgdir}/usr/share/applications
        install -d ${pkgdir}/usr/bin
        install -d ${pkgdir}/etc/skel/.config/autostart

	cp -r  ${srcdir}/kavach-help/xhelp/* "${pkgdir}/usr/bin/"
	cp -r ${srcdir}/kavach-help/xhelp/main.py "${pkgdir}/usr/bin/kavach-help"	
	chmod +x "${pkgdir}/usr/bin/kavach-help"

	cp -r ${srcdir}/kavach-help/khelp.desktop "${pkgdir}/etc/skel/.config/autostart/kavach-help.desktop"
	chmod +x "${pkgdir}/etc/skel/.config/autostart/kavach-help.desktop"
     
	cp -r ${srcdir}/kavach-help/khelp.desktop "${pkgdir}/usr/share/applications/kavach-help.desktop"
}

