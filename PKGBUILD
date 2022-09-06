pkgname=kavach-xhelp
pkgver=0.0.1
pkgrel=1
epoch=
pkgdesc="Cyber Helpline App for Kavach OS"
arch=(x86_64)
url=""
license=('GPL')
groups=()
depends=(PyQt5)
makedepends=(python-build)
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("$pkgname-$pkgver.tar.bz2")
noextract=()
md5sums=(SKIP)
validpgpkeys=()


build() {
        python -m build
}

package() {
        pip install --root="$pkgdir" dist/xedu-0.0.1.tar.gz
        install -Dm 755 helpr "$pkgdir"/usr/bin/helpr
        # install -Dm 655 khelp.desktop "$pkgdir"/usr/share/applications/khelp.desktop
}

