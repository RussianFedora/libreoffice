%define libo_version 3.4.5
# rhbz#715152 state vendor
%if 0%{?rhel}
%define vendoroption --with-vendor="Red Hat, Inc."
%endif
%if 0%{?fedora}
%define vendoroption --with-vendor="The Fedora Project"
%endif
# rhbz#465664 jar-repacking breaks help by reordering META-INF/MANIFEST.MF
%define __jar_repack %{nil}
# don't worry about whitespace for now
%define _default_patch_flags -s -l
# undef to get english only and no-langpacks for a faster smoketest build
%define langpacks 1
# make it easier to download sources from pre-release site
# http://dev-builds.libreoffice.org/pre-releases/src
#%%define source_url http://dev-builds.libreoffice.org/pre-releases/src
%define source_url http://download.documentfoundation.org/libreoffice/src/%{libo_version}

%if %{langpacks}
%if %{defined rhel} && 0%{?rhel} < 7
%define langpack_langs en-US af ar bg bn ca cs cy da de dz el es et eu fi fr ga gl gu he hi hr hu it ja ko lt mai ml mr ms nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh sk sl sr ss st sv ta te th tn tr ts uk ur ve xh zh-CN zh-TW zu
%else
%define langpack_langs en-US af ar as bg bn ca cs cy da de dz el es et eu fa fi fr ga gl gu he hi hr hu it ja ko kn lt lv mai ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-CN zh-TW zu
%endif
%define with_lang --with-lang="%{langpack_langs}"
%else
%define langpack_langs en-US
%define with_lang ''
%endif

Summary:        Free Software Productivity Suite
Name:           libreoffice
Epoch:          1
Version:        %{libo_version}.2
Release:        1%{?dist}.R
License:        LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and (CDDL or GPLv2) and Public Domain
Group:          Applications/Productivity
URL:            http://www.documentfoundation.org/develop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-artwork-%{version}.tar.bz2
Source1:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-base-%{version}.tar.bz2
Source2:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-bootstrap-%{version}.tar.bz2
Source3:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-calc-%{version}.tar.bz2
Source4:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-components-%{version}.tar.bz2
Source5:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-extensions-%{version}.tar.bz2
Source6:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-extras-%{version}.tar.bz2
Source7:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-filters-%{version}.tar.bz2
Source8:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-help-%{version}.tar.bz2
Source9:        http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-impress-%{version}.tar.bz2
Source10:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-libs-core-%{version}.tar.bz2
Source11:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-libs-extern-%{version}.tar.bz2
Source12:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-libs-extern-sys-%{version}.tar.bz2
Source13:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-libs-gui-%{version}.tar.bz2
Source14:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-postprocess-%{version}.tar.bz2
Source15:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-sdk-%{version}.tar.bz2
Source16:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-testing-%{version}.tar.bz2
Source17:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-ure-%{version}.tar.bz2
Source18:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-writer-%{version}.tar.bz2
Source19:       http://download.documentfoundation.org/libreoffice/src/3.4.5/libreoffice-translations-%{version}.tar.bz2
Source20:       http://download.go-oo.org/extern/185d60944ea767075d27247c3162b3bc-unowinreg.dll
Source21:       redhat-langpacks.tar.gz
Source22:       libreoffice-multiliblauncher.sh
Source23:       http://hg.services.openoffice.org/binaries/fdb27bfe2dbe2e7b57ae194d9bf36bab-SampleICC-1.3.2.tar.gz
Source24:       http://hg.services.openoffice.org/binaries/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source25:       http://hg.services.openoffice.org/binaries/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
Source26:       http://hg.services.openoffice.org/binaries/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source27:       http://hg.services.openoffice.org/binaries/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
Source28:       http://hg.services.openoffice.org/binaries/ada24d37d8d638b3d8a9985e80bc2978-source-9.0.0.7-bj.zip
Source29:       http://hg.services.openoffice.org/binaries/18f577b374d60b3c760a3a3350407632-STLport-4.5.tar.gz 
#Unfortunately later versions of hsqldb changed the file format, so if we use a later version we loose
#backwards compatability.
Source30:       http://hg.services.openoffice.org/binaries/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
Source31:       http://download.go-oo.org/extern/b4cae0700aa1c2aef7eb7f345365e6f1-translate-toolkit-1.8.1.tar.bz2
%if %{defined rhel} && 0%{?rhel} < 7
Source32:       http://dev-www.libreoffice.org/src/0ff7d225d087793c8c2c680d77aac3e7-mdds_0.5.3.tar.bz2
Source33:       http://hg.services.openoffice.org/binaries/067201ea8b126597670b5eff72e1f66c-mythes-1.2.0.tar.gz
%endif
BuildRequires:  zip, findutils, autoconf, flex, bison, icu, gperf, gcc-c++
BuildRequires:  binutils, java-devel < 1:1.7.0, boost-devel, zlib-devel
BuildRequires:  python-devel, expat-devel, libxml2-devel, libxslt-devel, bc
BuildRequires:  neon-devel, libcurl-devel, libidn-devel, pam-devel, cups-devel
BuildRequires:  libXext-devel, libXt-devel, libICE-devel, libjpeg-devel, make
BuildRequires:  gecko-devel, libwpd-devel, hunspell-devel, unixODBC-devel
BuildRequires:  db4-devel, sane-backends-devel, libicu-devel, perl(Archive::Zip)
BuildRequires:  freetype-devel, gtk2-devel, desktop-file-utils, hyphen-devel
BuildRequires:  evolution-data-server-devel, libtextcat-devel, nss-devel
BuildRequires:  gstreamer-devel, gstreamer-plugins-base-devel, openssl-devel
BuildRequires:  lpsolve-devel, bsh, lucene, lucene-contrib
BuildRequires:  mesa-libGLU-devel, redland-devel, ant, ant-apache-regexp, rsync
BuildRequires:  jakarta-commons-codec, jakarta-commons-httpclient, cppunit-devel
BuildRequires:  jakarta-commons-lang, poppler-devel, fontpackages-devel
BuildRequires:  pentaho-reporting-flow-engine, libXinerama-devel
BuildRequires:  vigra-devel
BuildRequires:  font(:lang=en)
BuildRequires:  liberation-mono-fonts
%if %{defined rhel} && 0%{?rhel} < 7
BuildRequires:  hsqldb
%else
BuildRequires:  mdds-devel, mythes-devel, graphite2-devel, libwpg-devel
BuildRequires:  libwps-devel, junit4, perl(Digest::MD5)
%endif
%if %{undefined rhel}
BuildRequires:  kdelibs4-devel
%endif

Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
Requires: %{name}-draw = %{epoch}:%{version}-%{release}
Requires: %{name}-math = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-emailmerge = %{epoch}:%{version}-%{release}
%if %{defined rhel} && 0%{?rhel} < 7
Obsoletes: openoffice.org < 1.9.0
%endif

Patch1:  openoffice.org-2.0.2.rh188467.printingdefaults.patch
Patch2:  openoffice.org-2.4.0.ooo86080.unopkg.bodge.patch
Patch3:  openoffice.org-3.0.0.ooo88341.sc.verticalboxes.patch
Patch4:  openoffice.org-3.1.0.oooXXXXX.solenv.allowmissing.patch
Patch5:  openoffice.org-3.1.0.ooo101274.opening-a-directory.patch
Patch6:  openoffice.org-3.1.1.ooo105784.vcl.sniffscriptforsubs.patch
Patch7:  openoffice.org-3.3.0.ooo108637.sfx2.uisavedir.patch
Patch8:  openoffice.org-3.3.0.ooo113273.desktop.resolvelinks.patch
Patch9:  libreoffice-installfix.patch
Patch10: 0001-helgrind-Related-rhbz-655686-get-order-of-shutdown-c.patch
Patch11: kde4configure.patch
Patch12: 0001-Resolves-rhbz-695509-crash-in-RefreshDocumentLB.patch
Patch13: 0001-bubble-down-configure-test-findings-on-visibility.patch
Patch14: vbahelper.visibility.patch
Patch15: 0001-rhbz-702635-set-correct-page-number-when-exporting-s.patch
Patch16: 0001-Related-rhbz-652604-better-survive-exceptions-thrown.patch
Patch17: 0001-Resolves-rhbz-713154-pdf-export-dialog-too-tall-to-f.patch
Patch18: 0001-Related-rhbz-702833-addEventListener-without-removeE.patch
Patch19: 0001-Related-rhbz-711087-band-aid.patch
Patch20: 0001-rhbz-667082-do-not-crash-importing-section-containin.patch
Patch21: 0001-Related-rhbz-718976-crash-in-SwTxtSizeInfo-GetMultiC.patch
Patch22: 0001-Resolves-rhbz-715549-use-fontconfig-s-detected-forma.patch
Patch23: 0001-Resolves-rhbz-693265-fix-crash-from-unhandled-except.patch
Patch24: 0001-Related-rhbz-730225-avoid-segv-in-ld-this-was-set-to.patch
Patch25: gdb-pretty-printers.patch
Patch26: 0001-Related-fdo-37195-migrationoo3-not-registered.patch
Patch27: 0001-Resolves-rhbz-738255-avoid-crash-on-NULL-pointer.patch
Patch28: 0001-Resolves-rhbz-751290-KDE-black-on-dark-tooltips.patch
Patch29: 0001-gtk3-fix-cairo-canvas-crash-for-non-X-or-svp-backend.patch
Patch30: 0001-Resolves-rhbz-759647-dispose-clears-mpPresTimer-befo.patch
Patch31: 0001-Resolves-rhbz-761009-IFSD_Equal-is-asymmetrical.patch
Patch32: 0001-Resolves-rhbz-767708-avoid-SIGBUS-writing-to-overcom.patch
Patch33: 0001-smath-does-not-handle-accents-in-MathML.patch
Patch34: 0001-fix-writing-of-strings-from-the-first-module.patch
Patch35: 0001-Confine-JDBC-driver-to-thread-affine-apartment-for-J.patch
%if %{defined rhel} && 0%{?rhel} < 7
Patch36: libreoffice-libwpd08-1.patch
Patch37: libreoffice-libwpd08-2.patch
Patch38: 0001-wpsimport-writerperfect.diff-WPS-Import-filter-core-.patch
Patch39: libreoffice-gcj.patch
Patch40: libreoffice-rhel6poppler.patch
Patch41: libreoffice-rhel6langs.patch
%endif
Patch42: solenv.fix.mk.inheritance.patch
Patch43: 0001-Related-rhbz-753201-fedora-ant-java-1.5.0-gcj-won-t-.patch
Patch44: 0001-Resolves-fdo-44078-fix-unfortunate-name-alias-mixups.patch

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define instdir %{_libdir}
%define baseinstdir %{instdir}/libreoffice
%define ureinstdir %{baseinstdir}/ure
%define basisinstdir %{baseinstdir}/basis3.4
%define sdkinstdir %{baseinstdir}/basis3.4/sdk
%define fontname opensymbol
%define OFFICEUPD 340
%define SOPOST l*

%description
LibreOffice is an Open Source, community-developed, office productivity suite.
It includes the key desktop applications, such as a word processor,
spreadsheet, presentation manager, formula editor and drawing program, with a
user interface and feature set similar to other office suites.  Sophisticated
and flexible, LibreOffice also works transparently with a variety of file
formats, including Microsoft Office File Formats.

%package core
Summary: Core modules for LibreOffice
Group: Applications/Productivity
Requires: %{name}-%{fontname}-fonts = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: liberation-sans-fonts >= 1.0, liberation-serif-fonts >= 1.0, liberation-mono-fonts >= 1.0
Requires: dejavu-sans-fonts, dejavu-serif-fonts, dejavu-sans-mono-fonts
Requires: hunspell-en, hyphen-en, hyphen >= 2.4, autocorr-en
Requires: lucene
Requires(pre):    gtk2 >= 2.9.4
Requires(post):   gtk2 >= 2.9.4
Requires(preun):  gtk2 >= 2.9.4
Requires(postun): gtk2 >= 2.9.4
Obsoletes: openoffice.org-core < 1:3.3.1
Obsoletes: openoffice.org-brand < 1:3.3.1, broffice.org-brand < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-core = 1:3.3.0
Provides: openoffice.org-brand = 1:3.3.0, broffice.org-brand = 1:3.3.0
Obsoletes: openoffice.org-libs < 1.9.0
Obsoletes: openoffice.org-i18n < 1.9.0
Obsoletes: openoffice.org-kde < 1.9.0
Obsoletes: openoffice.org-langpack-eo < 1:2.0.0
Obsoletes: openoffice.org2-core < 1:3.0.0
%else
Obsoletes: openoffice.org-langpack-ms < 1:3.3.1, libreoffice-langpack-ms < 1:3.3.99.1
Obsoletes: openoffice.org-langpack-ur < 1:3.3.1, libreoffice-langpack-ur < 1:3.3.99.1
%endif

%description core
The shared core libraries and support files for LibreOffice.

%package pyuno
Summary: Python support for LibreOffice
Group: Development/Libraries
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: python
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-pyuno < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-pyuno = 1:3.3.0
Obsoletes: openoffice.org2-pyuno < 1:3.0.0
%endif

%description pyuno
Python bindings for the LibreOffice UNO component model. Allows scripts both
external to LibreOffice and within the internal LibreOffice scripting framework
to be written in python.

%package base
Summary: Database front-end for LibreOffice
Group: Applications/Productivity
Requires: postgresql-jdbc
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-base-core < 1:3.3.1
Obsoletes: openoffice.org-base < 1:3.3.1, broffice.org-base < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-base-core = 1:3.3.0
Provides: openoffice.org-base = 1:3.3.0, broffice.org-base = 1:3.3.0
Obsoletes: openoffice.org2-base < 1:3.0.0
%endif

%description base
GUI database front-end for LibreOffice. Allows creation and management of 
databases through a GUI.

%package report-builder
Summary: Create database reports from LibreOffice
Group: Applications/Productivity
Requires: pentaho-reporting-flow-engine
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-report-builder < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-report-builder = 1:3.3.0
%endif

%description report-builder
Creates database reports from LibreOffice databases. The report builder can
define group and page headers as well as group, page footers and calculation
fields to accomplish complex database reports.

%package bsh
Summary: BeanShell support for LibreOffice
Group: Development/Libraries
Requires: bsh
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-bsh < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-bsh = 1:3.3.0
%endif

%description bsh
Support BeanShell scripts in LibreOffice.

%package rhino
Summary: JavaScript support for LibreOffice
Group: Development/Libraries
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-rhino < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-rhino = 1:3.3.0
%endif

%description rhino
Support JavaScript scripts in LibreOffice.

%package wiki-publisher
Summary: Create Wiki articles on MediaWiki servers with LibreOffice
Group: Applications/Productivity
Requires: jakarta-commons-codec, jakarta-commons-httpclient
Requires: jakarta-commons-lang, jakarta-commons-logging
Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-wiki-publisher < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-wiki-publisher = 1:3.3.0
%endif

%description wiki-publisher
The Wiki Publisher enables you to create Wiki articles on MediaWiki servers
without having to know the syntax of the MediaWiki markup language. Publish
your new and existing documents transparently with writer to a wiki page.

%package ogltrans
Summary: 3D OpenGL slide transitions for LibreOffice
Group: Applications/Productivity
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Obsoletes: openoffice.org-ogltrans < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-ogltrans = 1:3.3.0
%endif

%description ogltrans
OpenGL Transitions enable 3D slide transitions to be used in LibreOffice.
Requires good quality 3D support for your graphics card for best experience.

%package presentation-minimizer
Summary: Shrink LibreOffice presentations
Group: Applications/Productivity
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-presentation-minimizer < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-presentation-minimizer = 1:3.3.0
%endif

%description presentation-minimizer
The Presentation Minimizer is used to reduce the file size of the current
presentation. Images will be compressed, and data that is no longer needed will
be removed.

%package presenter-screen
Summary: Presenter Screen for LibreOffice Presentations
Group: Applications/Productivity
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-presenter-screen < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-presenter-screen = 1:3.3.0
%endif

%description presenter-screen
The Presenter Screen is used to provides information on a second screen, that
typically is not visible to the audience when delivering a presentation. e.g.
slide notes.

%package pdfimport
Summary: PDF Importer for LibreOffice Draw
Group: Applications/Productivity
Requires: %{name}-draw = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-pdfimport < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-pdfimport = 1:3.3.0
%endif

%description pdfimport
The PDF Importer imports PDF into drawing documents to preserve layout
and enable basic editing of PDF documents.

%package %{fontname}-fonts
Summary: LibreOffice dingbats font
Group: User Interface/X
Requires: fontpackages-filesystem
Obsoletes: openoffice.org-fonts < 1:3.3.1
Obsoletes: openoffice.org-opensymbol-fonts < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-fonts = 1:3.3.0
Provides: openoffice.org-opensymbol-fonts = 1:3.3.0
%endif
BuildArch: noarch

%description %{fontname}-fonts
A dingbats font, OpenSymbol, suitable for use by LibreOffice for bullets and
mathematical symbols. 

%package writer
Summary: LibreOffice Word Processor Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-writer-core < 1:3.3.1
Obsoletes: openoffice.org-writer < 1:3.3.1, broffice.org-writer < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-writer-core = 1:3.3.0
Provides: openoffice.org-writer = 1:3.3.0, broffice.org-writer = 1:3.3.0
Obsoletes: openoffice.org2-writer < 1:3.0.0
%endif

%description writer
The LibreOffice Word Processor application.

%package emailmerge
Summary: Email mail-merge component for LibreOffice 
Group: Applications/Productivity
Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-pyuno = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-emailmerge < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-emailmerge = 1:3.3.0
Obsoletes: openoffice.org2-emailmerge < 1:3.0.0
%endif

%description emailmerge
Enables the LibreOffice writer module to mail-merge to email.

%package calc
Summary: LibreOffice Spreadsheet Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-calc-core < 1:3.3.1
Obsoletes: openoffice.org-calc < 1:3.3.1, broffice.org-calc < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-calc-core = 1:3.3.0
Provides: openoffice.org-calc = 1:3.3.0, broffice.org-calc = 1:3.3.0
%endif

%description calc
The LibreOffice Spreadsheet application.

%package draw
Summary: LibreOffice Drawing Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-pdfimport = %{epoch}:%{version}-%{release}
Requires: %{name}-graphicfilter = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-draw-core < 1:3.3.1
Obsoletes: openoffice.org-draw < 1:3.3.1, broffice.org-draw < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-draw-core = 1:3.3.0
Provides: openoffice.org-draw = 1:3.3.0, broffice.org-draw = 1:3.3.0
Obsoletes: openoffice.org2-draw < 1:3.0.0
%endif

%description draw
The LibreOffice Drawing Application.

%package impress
Summary: LibreOffice Presentation Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-presenter-screen = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-impress-core < 1:3.3.1
Obsoletes: openoffice.org-impress < 1:3.3.1, broffice.org-impress < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-impress-core = 1:3.3.0
Provides: openoffice.org-impress = 1:3.3.0, broffice.org-impress = 1:3.3.0
Obsoletes: openoffice.org2-impress < 1:3.0.0
%endif

%description impress
The LibreOffice Presentation Application.

%package math
Summary: LibreOffice Equation Editor Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-math-core < 1:3.3.1
Obsoletes: openoffice.org-math < 1:3.3.1, broffice.org-math < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-math-core = 1:3.3.0
Provides: openoffice.org-math = 1:3.3.0, broffice.org-math = 1:3.3.0
Obsoletes: openoffice.org2-math < 1:3.0.0
%endif

%description math 
The LibreOffice Equation Editor Application.

%package graphicfilter
Summary: LibreOffice Extra Graphic filters
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-graphicfilter < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-graphicfilter = 1:3.3.0
Obsoletes: openoffice.org2-graphicfilter < 1:3.0.0
%endif

%description graphicfilter
The graphicfilter module for LibreOffice provides graphic filters, e.g. svg and
flash filters.

%package xsltfilter
Summary: Optional xsltfilter module for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-xsltfilter < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-xsltfilter = 1:3.3.0
Obsoletes: openoffice.org2-xsltfilter < 1:3.0.0
%endif

%description xsltfilter
The xsltfilter module for LibreOffice, provides additional docbook and
xhtml export transforms. Install this to enable docbook export.

%package javafilter
Summary: Optional javafilter module for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-javafilter < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-javafilter = 1:3.3.0
Obsoletes: openoffice.org2-javafilter < 1:3.0.0
%endif

%description javafilter
The javafilter module for LibreOffice, provides additional AportisDoc,
Pocket Excel and Pocket Word import filters.

%post javafilter
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun javafilter
update-desktop-database %{_datadir}/applications &> /dev/null || :

%package testtools
Summary: Testtools for LibreOffice
Group: Development/Libraries
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}
Requires: %{name}-draw = %{epoch}:%{version}-%{release}
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-math = %{epoch}:%{version}-%{release}
Requires: %{name}-bsh = %{epoch}:%{version}-%{release}
Requires: %{name}-rhino = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-testtools < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-testtools = 1:3.3.0
Obsoletes: openoffice.org2-testtools < 1:3.0.0
%endif

%description testtools
QA tools for LibreOffice, enables automated testing.

%package ure
Summary: UNO Runtime Environment
Group: Development/Libraries
Requires: unzip, jre >= 1.5.0
Obsoletes: openoffice.org-ure < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-ure = 1:3.3.0
%endif

%description ure
UNO is the component model of LibreOffice. UNO offers interoperability between
programming languages, other components models and hardware architectures,
either in process or over process boundaries, in the Intranet as well as in the
Internet. UNO components may be implemented in and accessed from any
programming language for which a UNO implementation (AKA language binding) and
an appropriate bridge or adapter exists

%package sdk
Summary: Software Development Kit for LibreOffice
Group: Development/Libraries
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: unzip, java-devel
Obsoletes: openoffice.org-sdk < 1:3.3.1, openoffice.org-devel < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-sdk = 1:3.3.0, openoffice.org-devel = 1:3.3.0
%endif

%description sdk
The LibreOffice SDK is an add-on for the LibreOffice office suite. It provides
the necessary tools for programming using the LibreOffice APIs and for creating
extensions (UNO components) for LibreOffice.  To set the build environment for
building against the sdk use %{sdkinstdir}/setsdkenv_unix.sh.

%package sdk-doc
Summary: Software Development Kit documentation for LibreOffice
Group: Documentation
Requires: %{name}-sdk = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-sdk-doc < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-sdk-doc = 1:3.3.0
%endif

%description sdk-doc
This provides documentation for programming using the LibreOffice APIs
and examples of creating extensions (UNO components) for LibreOffice.

%package headless
Summary: LibreOffice Headless plug-in
Group: Development/Libraries
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Obsoletes: openoffice.org-headless < 1:3.3.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-headless = 1:3.3.0
%endif

%description headless
A plug-in for LibreOffice that enables it to function without an X server. 
It implements the -headless command line option and allows LibreOffice to be
used as a backend server for e.g. document conversion.

%if %{undefined rhel}
%package kde
Summary: LibreOffice KDE integration plug-in
Group:   Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}

%description kde
A plug-in for LibreOffice that enables integration into the KDE desktop environment.
%endif

%if 0%{?_enable_debug_packages}

%define debug_package %{nil}
%global __debug_package 1

%package debuginfo
Summary: Debug information for package %{name}
Group: Development/Debug
AutoReqProv: 0
Requires: libreoffice-core = %{epoch}:%{version}-%{release}
Requires: libreoffice-gdb-debug-support = %{epoch}:%{version}-%{release}

%description debuginfo
This package provides debug information for package %{name}.
Debug information is useful when developing applications that use this
package or when debugging this package.

%files debuginfo -f debugfiles.list
%defattr(-,root,root)

%package gdb-debug-support
Summary: Additional support for debugging with gdb
Group: Development/Debug
Requires: gdb
AutoReqProv: 0

%description gdb-debug-support
This package provides gdb pretty printers for package %{name}.

%files gdb-debug-support
%defattr(-,root,root)
%{_datadir}/gdb/auto-load%{baseinstdir}
%{_datadir}/libreoffice/gdb

%endif

# Defines a language pack subpackage.
#
# It's necessary to define language code (-l) and language name (-n).
# Additionally, it's possible
# * to require autocorr, hunspell, hyphen or mythes package or font for
#   given language,
# * to obsolete openoffice.org-langpack package,
# * to provide libreoffice-langpack-loc package, where loc is glibc
#   locale--this is necessary for yum to pick it automatically,
# * to require other, unrelated, packages,
# * to specify file serving as file list.
# For these, lower case character argument takes an argument specifying
# language, upper case character argument uses language from -l.
#
# All remaining arguments are considered to be files and added to the file
# list.
#
# Aa: autocorr dependency
# Ff: font language dependency
# Hh: hunspell dependency
# l:  language code, e.g., cs
# Mm: mythes dependency
# n:  language name, e.g., Czech
# Oo: Obsoletes: of openoffice.org-langpack
# Vv: Very archaic Obsoletes: of openoffice.org-langpack
# Xx: Archaic Obsoletes: of openoffice.org2-langpack
# p:  Provides: of libreoffice-langpack
# r:  comma-separated list of additional requires
# Ss: filelist
# Yy: hyphen dependency
#
# Example:
# libreoffice-langpack-cs: langpack for Czech lang. requiring hyphen-cs,
# autocorr-cs, mythes-cs-CZ and suitable font, obsoleting
# openoffice.org-langpack-cs_CZ, and taking the files from cs.filelist:
# %langpack -l cs -n Czech -H -A -m cs-CZ -o cs_CZ -S
%define langpack(Aa:Ff:Hh:l:Mm:n:Oo:p:r:Ss:Vv:Xx:Yy:) \
%define project LibreOffice \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %{project} \
Group: Applications/Productivity \
Requires: %{name}-core = %{epoch}:%{version}-%{release} \
%{-a:Requires: autocorr-%{-a*}}%{!-a:%{-A:Requires: autocorr-%{lang}}} \
%{-f:Requires: font(:lang=%{-f*})}%{!-f:%{-F:Requires: font(:lang=%{lang})}} \
%{-h:Requires: hunspell-%{-h*}}%{!-h:%{-H:Requires: hunspell-%{lang}}} \
%{-m:Requires: mythes-%{-m*}}%{!-m:%{-M:Requires: mythes-%{lang}}} \
%{-y:Requires: hyphen-%{-y*}}%{!-y:%{-Y:Requires: hyphen-%{lang}}} \
%{-r:Requires: %{-r*}} \
%define obs openoffice.org-langpack \
%define obsv 1:3.3.1 \
%define aobs openoffice.org2-langpack \
%define aobsv 1:3.0.0 \
%define vaobs openoffice.org-langpack \
%define vaobsv 1:2.0.3 \
%if %{defined rhel} && 0%{?rhel} < 7 \
%{-o: \
Obsoletes: openoffice.org-i18n < 1.9.0 \
Obsoletes: %{obs}-%{-o*} < %{obsv} \
Provides: %{obs}-%{-o*} = 1:3.3.0  \
}%{!-o: \
%{-O: \
Obsoletes: openoffice.org-i18n < 1.9.0 \
Obsoletes: %{obs}-%{lang} < %{obsv} \
Provides: %{obs}-%{lang} = 1:3.3.0  \
}} \
%else \
%{-o:Obsoletes: %{obs}-%{-o*} < %{obsv}}%{!-o:%{-O:Obsoletes: %{obs}-%{lang} < %{obsv}}} \
%endif \
%{-x:Obsoletes: %{aobs}-%{-x*} < %{aobsv}}%{!-x:%{-X:Obsoletes: %{aobs}-%{lang} < %{aobsv}}} \
%{-v:Obsoletes: %{vaobs}-%{-v*} < %{vaobsv}}%{!-v:%{-V:Obsoletes: %{vaobs}-%{lang} < %{vaobsv}}} \
%{-p:Provides: %{name}-langpack-%{-p*}} \
\
%description %{pkgname} \
Provides additional %{langname} translations and resources for %{project}. \
\
%define filelist %{-s:-f %{-s*}.filelist}%{!-s:%{-S:-f %{lang}.filelist}} \
%files %{pkgname} %{filelist} \
%defattr(-,root,root,-) \
%*


# Defines an auto-correction subpackage.
#
# l: language code
# n: language name
# X  do not use default file match on %{_datadir}/autocorr/acor_%{lang}-*
#    in file list
#
# All remaining arguments are considered to be files and added to the file
# list.
%define autocorr(l:n:X) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname autocorr-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package -n %{pkgname} \
Summary: %{langname} auto-correction rules \
Group: Applications/Text \
BuildArch: noarch \
\
%description -n %{pkgname} \
Rules for auto-correcting common %{langname} typing errors. \
\
%files -n %{pkgname} \
%defattr(-,root,root,-) \
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE \
%dir %{_datadir}/autocorr \
%{!-X:%{_datadir}/autocorr/acor_%{lang}-*} \
%*


%if %{langpacks}

%langpack -l af -n Afrikaans -F -H -Y -A -o af_ZA -V -x af_ZA -S
%langpack -l ar -n Arabic -F -H -O -X -S
%langpack -l as -n Assamese -F -H -Y -o as_IN -x as_IN -S
%langpack -l bg -n Bulgarian -F -H -Y -M -A -o bg_BG -V -x bg_BG -S
%langpack -l bn -n Bengali -F -H -Y -O -v bn_IN -X -S
%langpack -l ca -n Catalan -F -H -Y -M -o ca_ES -V -x ca_ES -S
%langpack -l cs -n Czech -F -H -Y -M -A -o cs_CZ -V -x cs_CZ -S
%langpack -l cy -n Welsh -F -H -Y -o cy_GB -V -x cy_GB -S
%langpack -l da -n Danish -F -H -Y -M -A -o da_DK -V -x da_DK -S
%langpack -l de -n German -F -H -Y -M -A -O -X -S
%langpack -l dz -n Dzongkha -F -O -S
%langpack -l el -n Greek -F -H -Y -M -o el_GR -V -x el_GR -S
%langpack -l en -n English -M -O
%langpack -l es -n Spanish -F -H -Y -M -A -O -X -S
%langpack -l et -n Estonian -F -H -Y -o et_EE -V -x et_EE -S
%langpack -l eu -n Basque -F -H -Y -A -o eu_ES -V -x eu_ES -S
%langpack -l fa -n Farsi -A -H -Y -S
%if %{defined rhel} && 0%{?rhel} < 7
%langpack -l fi -n Finnish -F -A -o fi_FI -V -x fi_FI -S
%else
%langpack -l fi -n Finnish -F -r openoffice.org-voikko -A -o fi_FI -S
%endif
%langpack -l fr -n French -F -H -Y -M -A -O -X -S
%langpack -l ga -n Irish -F -H -Y -M -A -o ga_IE -x ga_IE -S
%langpack -l gl -n Galician -F -H -Y -o gl_ES -V -x gl_ES -S
%langpack -l gu -n Gujarati -F -H -Y -o gu_IN -x gu_IN -S
%langpack -l he -n Hebrew -F -H -o he_IL -V -x he_IL -S
%langpack -l hi -n Hindi -F -H -Y -o hi_IN -v hi_IN -x hi_IN -S
%langpack -l hr -n Croatian -F -H -Y -A -o hr_HR -V -x hr_HR -S
%langpack -l hu -n Hungarian -F -H -Y -M -A -o hu_HU -V -x hu_HU -S
%langpack -l it -n Italian -F -H -Y -M -A -O -X -S
%langpack -l ja -n Japanese -F -A -o ja_JP -V -x ja_JP -S
%langpack -l kn -n Kannada -F -H -Y -o kn_IN -x ka_IN -S
%langpack -l ko -n Korean -F -H -A -o ko_KR -V -x ko_KR -S
%{baseinstdir}/share/registry/korea.xcd

%langpack -l lt -n Lithuanian -F -H -Y -A -o lt_LT -V -x lt_LT -S
%langpack -l lv -n Latvian -F -H -Y -M -S
%langpack -l mai -n Maithili -F -o mai_IN -S
%langpack -l ml -n Malayalam -F -H -Y -o ml_IN -x ml_IN -S
%langpack -l mr -n Marathi -F -H -Y -o mr_IN -x mr_IN -S
%if %{defined rhel} && 0%{?rhel} < 7
%langpack -l ms -n Malay -F -H -o ms_MY -V -x ms_MY -S
%endif
%langpack -l nb -n Bokmal -F -H -Y -M -o nb_NO -V -x nb_NO -S
%langpack -l nl -n Dutch -F -H -Y -M -A -O -X -S
%langpack -l nn -n Nynorsk -F -H -Y -M -o nn_NO -V -x nn_NO -S
%define langpack_lang Southern Ndebele
%langpack -l nr -n %{langpack_lang} -F -H -o nr_ZA -S
%define langpack_lang Northern Sotho
%langpack -l nso -n %{langpack_lang} -F -H -o nso_ZA -x nso_ZA -S
%langpack -l or -n Oriya -F -H -Y -o or_IN -x or_IN -S
%langpack -l pa -n Punjabi -F -H -Y -O -v pa_IN -x pa_IN -s pa-IN
%langpack -l pl -n Polish -F -H -Y -M -A -o pl_PL -V -x pl_PL -S
%define langpack_lang Brazilian Portuguese
%langpack -l pt-BR -n %{langpack_lang} -f pt -h pt -y pt -m pt -a pt -o pt_BR -p pt_BR -V -X -S
%langpack -l pt-PT -n Portuguese -f pt -h pt -y pt -m pt -a pt -o pt_PT -p pt_PT -v pt -X -s pt
%langpack -l ro -n Romanian -F -H -Y -M -O -S
%langpack -l ru -n Russian -F -H -Y -M -A -O -X -S
%langpack -l si -n Sinhalese -F -H -O -S
%langpack -l sk -n Slovak -F -H -Y -M -A -o sk_SK -V -x sk_SK -S
%langpack -l sl -n Slovenian -F -H -Y -M -A -o sl_SI -V -x sl_SI -S
%langpack -l sr -n Serbian -F -H -Y -A -O -v sr_CS -x sr_CS -S
%langpack -l ss -n Swati -F -H -o ss_ZA -S
%define langpack_lang Southern Sotho
%langpack -l st -n %{langpack_lang} -F -H -o st_ZA -S
%langpack -l sv -n Swedish -F -H -Y -M -A -O -X -S
%langpack -l ta -n Tamil -F -H -Y -o ta_IN -x ta_IN -S
%langpack -l te -n Telugu -F -H -Y -o te_IN -x te_IN -S
%langpack -l th -n Thai -F -H -o th_TH -V -x th_TH -S
%langpack -l tn -n Tswana -F -H -o tn_ZA -V -x tn_ZA -S
%langpack -l tr -n Turkish -F -A -o tr_TR -V -x tr_TR -S
%langpack -l ts -n Tsonga -F -H -o ts_ZA -V -x ts_ZA -S
%langpack -l uk -n Ukrainian -F -H -Y -M -O -S
%if %{defined rhel} && 0%{?rhel} < 7
%langpack -l ur -n Urdu -F -H -O -X -S
%endif
%langpack -l ve -n Venda -F -H -o ve_ZA -S
%langpack -l xh -n Xhosa -F -H -o xh_ZA -S
%define langpack_lang Simplified Chinese
%langpack -l zh-Hans -n %{langpack_lang} -f zh-cn -a zh -o zh_CN -p zh_CN -v zh_CN -x zh_CN -s zh-CN
%define langpack_lang Traditional Chinese
%langpack -l zh-Hant -n %{langpack_lang} -f zh-tw -a zh -o zh_TW -p zh_TW -v zh_TW -x zh_TW -s zh-TW
%langpack -l zu -n Zulu -F -H -Y -o zu_ZA -V -x zu_ZA -S
%undefine langpack_lang

%endif

%autocorr -l en -n English

%if %{langpacks}

%autocorr -l af -n Afrikaans
%autocorr -l bg -n Bulgarian
%autocorr -l cs -n Czech
%autocorr -l da -n Danish
%autocorr -l de -n German
%autocorr -l es -n Spanish
%autocorr -l eu -n Basque -X
%{_datadir}/autocorr/acor_eu.dat

%autocorr -l fa -n Farsi
%autocorr -l fi -n Finnish
%autocorr -l fr -n French
%autocorr -l ga -n Irish
%autocorr -l hr -n Croatian
%autocorr -l hu -n Hungarian
%autocorr -l it -n Italian
%autocorr -l ja -n Japanese
%autocorr -l ko -n Korean
%autocorr -l lb -n Luxembourgish
%autocorr -l lt -n Lithuanian
%autocorr -l mn -n Mongolian
%autocorr -l nl -n Dutch
%autocorr -l pl -n Polish
%autocorr -l pt -n Portuguese
%autocorr -l ru -n Russian
%autocorr -l sk -n Slovak
%autocorr -l sl -n Slovenian
%autocorr -l sr -n Serbian
%{_datadir}/autocorr/acor_sh-*

%autocorr -l sv -n Swedish
%autocorr -l tr -n Turkish
%autocorr -l vi -n Vietnamese
%autocorr -l zh -n Chinese

%endif

%prep
%setup -q -c -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19
for a in */*; do mv `pwd`/$a .; done
#Customize Palette to remove Sun colours and add Red Hat colours
(head -n -1 extras/source/palettes/standard.soc && \
 echo -e ' <draw:color draw:name="Red Hat 1" draw:color="#cc0000"/>
 <draw:color draw:name="Red Hat 2" draw:color="#0093d9"/> 
 <draw:color draw:name="Red Hat 3" draw:color="#ff8d00"/>
 <draw:color draw:name="Red Hat 4" draw:color="#abb400"/>
 <draw:color draw:name="Red Hat 5" draw:color="#4e376b"/>' && \
 tail -n 1 extras/source/palettes/standard.soc) > redhat.soc
mv -f redhat.soc extras/source/palettes/standard.soc
%patch1  -p1
%patch2  -p1 -b .ooo86080.unopkg.bodge.patch
%patch3  -p1 -b .ooo88341.sc.verticalboxes.patch
%patch4  -p1 -b .oooXXXXX.solenv.allowmissing.patch
%patch5  -p0 -b .ooo101274.opening-a-directory.patch
%patch6  -p0 -b .ooo105784.vcl.sniffscriptforsubs.patch
%patch7  -p1 -b .ooo108637.sfx2.uisavedir.patch
%patch8  -p0 -b .ooo113273.desktop.resolvelinks.patch
%patch9  -p1 -b .libreoffice-installfix.patch
%patch10 -p1 -b .rhbz655686-get-order-of-shutdown-c.patch
%patch11 -p0 -b .kde4configure.patch
%patch12 -p1 -b .rhbz695509-crash-in-RefreshDocumentLB.patch
%patch13 -p1 -b .bubble-down-configure-test-findings-on-visibility.patch
%patch14 -p0 -b .vbahelper.visibility.patch
%patch15 -p1 -b .rhbz702635-set-correct-page-number-when-exporting-s.patch
%patch16 -p1 -b .rhbz652604-better-survive-exceptions-thrown.patch
%patch17 -p1 -b .rhbz713154-pdf-export-dialog-too-tall-to-f.patch
%patch18 -p1 -b .rhbz702833-addEventListener-without-removeE.patch
%patch19 -p1 -b .rhbz711087-band-aid.patch
%patch20 -p1 -b .rhbz667082-do-not-crash-importing-section-containin.patch
%patch21 -p1 -b .rhbz718976-crash-in-SwTxtSizeInfo-GetMultiC.patch
%patch22 -p1 -b .rhbz715549-use-fontconfig-s-detected-forma.patch
%patch23 -p1 -b .rhbz693265-fix-crash-from-unhandled-except.patch
%patch24 -p1 -b .rhbz730225-avoid-segv-in-ld-this-was-set-to.patch
%patch25 -p1
%patch26 -p1 -b .fdo37195-migrationoo3-not-registered.patch
%patch27 -p1 -b .rhbz738255-avoid-crash-on-NULL-pointer.patch
%patch28 -p1 -b .rhbz751290-KDE-black-on-dark-tooltips.patch
%patch29 -p1 -b .gtk3-fix-cairo-canvas-crash-for-non-X-or-svp-backend.patch
%patch30 -p1 -b .rhbz759647-dispose-clears-mpPresTimer-befo.patch
%patch31 -p1 -b .rhbz761009-IFSD_Equal-is-asymmetrical.patch
%patch32 -p1 -b .rhbz-767708-avoid-SIGBUS-writing-to-overcom.patch
%patch33 -p1 -b .smath-does-not-handle-accents-in-MathML.patch
%patch34 -p1 -b .fix-writing-of-strings-from-the-first-module.patch
%patch35 -p1 -b .Confine-JDBC-driver-to-thread-affine-apartment-for-J.patch
%if %{defined rhel} && 0%{?rhel} < 7
%patch36 -p1 -b .libwpd08-1.patch
%patch37 -p1 -R -b .libreoffice-libwpd08-2.patch
%patch38 -p1 -R -b .wpsimport
%patch39 -p1 -b .gcj.patch
%patch40 -p0 -b .rhel6poppler.patch
%patch41 -p0 -b .rhel6langs.patch
%endif
%patch42 -p1 -b .solenv.fix.mk.inheritance.patch
%patch43 -p1 -b .rhbz-753201-fedora-ant-java-1.5.0-gcj-won-t-.patch
%patch44 -p1 -b .fdo44078-fix-unfortunate-name-alias-mixups.patch

# these are horribly incomplete--empty translations and copied english
# strings with spattering of translated strings
rm -rf translations/source/{gu,he,hr}/helpcontent2
chmod +x solenv/bin/install-gdb-printers

%build
echo build start time is `date`, diskspace: `df -h . | tail -n 1`
#don't build localized helps which aren't translated
POORHELPS=`ls -d translations/source/*/helpcontent2 translations/source/*|cut -f 3 -d /|sort|uniq -u|xargs`
#don't build localized helps which are poorly translated
POORHELPS="$POORHELPS `grep 'msgstr .Working with Documents' translations/source/*/helpcontent2/source/text/swriter/guide.po| cut -f 3 -d / | xargs`"
#convert _smp_mflags to dmake equivalent
SMP_MFLAGS=%{?_smp_mflags}
SMP_MFLAGS=$[${SMP_MFLAGS/-j/}]
if [ $SMP_MFLAGS -lt 2 ]; then SMP_MFLAGS=2; fi
NDMAKES=`dc -e "$SMP_MFLAGS v p"`
NBUILDS=`dc -e "$SMP_MFLAGS $NDMAKES / p"`

%if %{undefined rhel}
# KDE bits
export QT4DIR=%{_qt4_prefix}
export KDE4DIR=%{_kde4_prefix}
export PATH=$QT4DIR/bin:$PATH
%endif

#use the RPM_OPT_FLAGS but remove the OOo overridden ones
for i in $RPM_OPT_FLAGS; do
        case "$i" in
                -O?|-pipe|-Wall|-g|-fexceptions) continue;;
        esac
        ARCH_FLAGS="$ARCH_FLAGS $i"
done
export ARCH_FLAGS
export CFLAGS=$ARCH_FLAGS
export CXXFLAGS=$ARCH_FLAGS

%if %{defined rhel}
%if 0%{?rhel} < 7
%define distrooptions --disable-graphite --without-system-mythes --without-system-mdds --without-junit
%else
%define distrooptions --without-system-hsqldb
%endif
%else
%define distrooptions --without-system-hsqldb --enable-kde4
%endif

autoconf
%configure \
 %vendoroption --with-num-cpus=$NBUILDS --with-max-jobs=$NDMAKES \
 --with-build-version="Ver: %{version}-%{release}" --with-unix-wrapper=%{name} \
 --disable-ldap --disable-epm --disable-mathmldtd --disable-Xaw \
 --disable-gnome-vfs --enable-gio --enable-symbols --enable-lockdown \
 --enable-evolution2 --enable-cairo --enable-dbus --enable-opengl --enable-vba \
 --enable-binfilter --enable-ext-presenter-minimizer \
 --enable-ext-presenter-console --enable-ext-pdfimport \
 --enable-ext-wiki-publisher --enable-ext-report-builder \
 --enable-ext-scripting-beanshell --enable-ext-scripting-javascript \
 --enable-ext-scripting-python --with-system-libtextcat \
 --with-system-jfreereport --with-vba-package-format="builtin" \
 --with-system-libs --with-system-headers --with-system-mozilla \
 --with-system-mythes --with-system-dicts --with-system-apache-commons \
 --without-system-saxon --with-external-dict-dir=/usr/share/myspell \
 --without-myspell-dicts --without-fonts --without-ppds --without-afms \
 %{with_lang} --with-poor-help-localizations="$POORHELPS" \
 --with-external-tar=`pwd`/ext_sources --with-java-target-version=1.5 \
 --with-external-libtextcat-data --without-system-translate-toolkit \
 %{distrooptions}

mkdir -p ext_sources
cp %{SOURCE20} ext_sources
cp %{SOURCE23} ext_sources
cp %{SOURCE24} ext_sources
cp %{SOURCE25} ext_sources
cp %{SOURCE26} ext_sources
cp %{SOURCE27} ext_sources
cp %{SOURCE28} ext_sources
cp %{SOURCE29} ext_sources
cp %{SOURCE30} ext_sources
cp %{SOURCE31} ext_sources
%if %{defined rhel} && 0%{?rhel} < 7
cp %{SOURCE32} ext_sources
cp %{SOURCE33} ext_sources
%endif
touch src.downloaded

. ./*[Ee]nv.[Ss]et.sh
./bootstrap

cd instsetoo_native
if ! VERBOSE=true build --dlv_switch -link -P$NBUILDS --all -- -P$NDMAKES -s; then
    build --dlv_switch -link --all
fi

#generate the icons and mime type stuff
export DESTDIR=../../../output
export KDEMAINDIR=/usr
export GNOMEDIR=/usr
export GNOME_MIME_THEME=hicolor
cd ../sysui
cd unxlng*/misc/libreoffice
./create_tree.sh

echo build end time is `date`, diskspace: `df -h . | tail -n 1`


%define install_bundled_extension(f:n:) \
%define extname_ %{-n:%{-n*}}%{!-n:%{error:No extension name given}} \
%define filename_ %{-f:%{-f*}}%{!-f:%{extname_}.oxt} \
%define extdir_ $RPM_BUILD_ROOT/%{baseinstdir}/share/extensions \
install -d -m 755 %{extdir_}/%{extname_} \
unzip -d %{extdir_}/%{extname_} $SOLARVER/$INPATH/bin/%{filename_} \
find %{extdir_}/%{extname_} -type f -name '*.txt' -exec chmod -x '{}' \\;


%install
rm -rf $RPM_BUILD_ROOT
source ./Linux*Env.Set.sh
#figure out the icon version
export `grep "^PRODUCTVERSIONSHORT =" solenv/inc/productversion.mk | sed -e "s/ //g"`
export `grep "PRODUCTVERSION[ ]*=[ ]*" solenv/inc/productversion.mk | sed -e "s/ //g"`
#install
cd instsetoo_native/util
#direct install
mkdir -p $RPM_BUILD_ROOT/%{instdir}
export PKGFORMAT=installed
#don't duplicate english helpcontent about the place
unset DEFAULT_TO_ENGLISH_FOR_PACKING
if dmake openoffice_en-US; then
    ok=true
    break
else
    echo - ---dump log start---
    cat ../unx*.pro/LibreOffice/installed/logging/en-US/log_*_en-US.log
    echo - ---dump log end---
    ok=false
fi
if [ $ok == "false" ]; then
    exit 1
fi
mkdir -p $RPM_BUILD_ROOT/%{baseinstdir}
mv ../unxlng*.pro/LibreOffice/installed/install/en-US/* $RPM_BUILD_ROOT/%{baseinstdir}
chmod -R +w $RPM_BUILD_ROOT/%{baseinstdir}
%if %{langpacks}
dmake ooolanguagepack
rm -rf ../unxlng*.pro/LibreOffice_languagepack/installed/install/log
for langpack in ../unxlng*.pro/LibreOffice_languagepack/installed/install/*; do
  cp -rp $langpack/* $RPM_BUILD_ROOT/%{baseinstdir}
  rm -rf $langpack
done
%endif
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/share/prereg
#give a consistent javasettingsunopkginstall.xml
$RPM_BUILD_ROOT/%{baseinstdir}/program/unopkg list --bundled || :
export WITH_LANG="en-US"
dmake sdkoo
mv ../unxlng*.pro/LibreOffice_SDK/installed/install/en-US/*/sdk $RPM_BUILD_ROOT/%{sdkinstdir}
cd ../../

# unpack extensions
%install_bundled_extension -n pdfimport -f pdfimport/pdfimport.oxt
%install_bundled_extension -n presentation-minimizer -f minimizer/presentation-minimizer.oxt
%install_bundled_extension -n presenter-screen -f presenter/presenter-screen.oxt
%install_bundled_extension -n report-builder
%install_bundled_extension -n script-provider-for-beanshell
%install_bundled_extension -n script-provider-for-javascript
%install_bundled_extension -n script-provider-for-python
%install_bundled_extension -n wiki-publisher -f swext/wiki-publisher.oxt

#configure sdk
pushd $RPM_BUILD_ROOT/%{sdkinstdir}
    for file in setsdkenv_unix.csh setsdkenv_unix.sh ; do
        sed -e "s,@OO_SDK_NAME@,sdk," \
            -e "s,@OO_SDK_HOME@,%{sdkinstdir}," \
            -e "s,@OFFICE_HOME@,%{baseinstdir}," \
            -e "s,@OFFICE_BASE_HOME@,%{basisinstdir}," \
            -e "s,@OO_SDK_URE_HOME@,%{ureinstdir}," \
            -e "s,@OO_SDK_MAKE_HOME@,/usr/bin," \
            -e "s,@OO_SDK_ZIP_HOME@,/usr/bin," \
            -e "s,@OO_SDK_CPP_HOME@,/usr/bin," \
            -e "s,@OO_SDK_CC_55_OR_HIGHER@,," \
            -e "s,@OO_SDK_JAVA_HOME@,$JAVA_HOME," \
            -e "s,@OO_SDK_OUTPUT_DIR@,\$HOME," \
            -e "s,@SDK_AUTO_DEPLOYMENT@,NO," \
            $file.in > $file
        chmod 755 $file
    done
#fix permissions
    find examples -type f -exec chmod -x {} \;
popd

chmod -x $RPM_BUILD_ROOT/%{basisinstdir}/program/testtoolrc

#ensure a template dir for each lang
pushd $RPM_BUILD_ROOT/%{basisinstdir}/share/template
for I in %{langpack_langs}; do
    mkdir -p $I
done
popd

#Set some aliases to canonical autocorrect language files for locales with matching languages
pushd $RPM_BUILD_ROOT/%{basisinstdir}/share/autocorr

en_GB_aliases="en-AG en-AU en-BS en-BW en-BZ en-CA en-DK en-GH en-HK en-IE en-IN en-JM en-NG en-NZ en-SG en-TT"
for lang in $en_GB_aliases; do
        ln -sf acor_en-GB.dat acor_$lang.dat
done
en_US_aliases="en-PH"
for lang in $en_US_aliases; do
        ln -sf acor_en-US.dat acor_$lang.dat
done
#en-ZA exists and has a good autocorrect file with two or three extras that make sense for 
#neighbouring english speaking territories
en_ZA_aliases="en-NA en-ZW"
for lang in $en_ZA_aliases; do
        ln -sf acor_en-ZA.dat acor_$lang.dat
done
%if %{langpacks}
af_ZA_aliases="af-NA"
for lang in $af_ZA_aliases; do
        ln -sf acor_af-ZA.dat acor_$lang.dat
done
de_DE_aliases="de-AT de-BE de-CH de-LI de-LU"
for lang in $de_DE_aliases; do
        ln -sf acor_de-DE.dat acor_$lang.dat
done
es_ES_aliases="es-AR es-BO es-CL es-CO es-CR es-CU es-DO es-EC es-GT es-HN es-MX es-NI es-PA es-PE es-PR es-PY es-SV es-US es-UY es-VE"
for lang in $es_ES_aliases; do
        ln -sf acor_es-ES.dat acor_$lang.dat
done
fr_FR_aliases="fr-BE fr-CA fr-CH fr-LU fr-MC"
for lang in $fr_FR_aliases; do
        ln -sf acor_fr-FR.dat acor_$lang.dat
done
it_IT_aliases="it-CH"
for lang in $it_IT_aliases; do
        ln -sf acor_it-IT.dat acor_$lang.dat
done
nl_NL_aliases="nl-AW nl-BE"
for lang in $nl_NL_aliases; do
        ln -s acor_nl-NL.dat acor_$lang.dat
done
sv_SE_aliases="sv-FI"
for lang in $sv_SE_aliases; do
        ln -s acor_sv-SE.dat acor_$lang.dat
done
%else
rm -f acor_[a-df-z]*.dat acor_e[su]*.dat
%endif
popd
#rhbz#484055 make these shared across multiple applications
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv -f $RPM_BUILD_ROOT/%{basisinstdir}/share/autocorr $RPM_BUILD_ROOT/%{_datadir}/autocorr
chmod 755 $RPM_BUILD_ROOT/%{_datadir}/autocorr

%if %{langpacks}

#auto generate the langpack file lists, format is...
#langpack id, has help or not, autocorrection glob, script classification
langpackdetails=\
(\
af      nohelp  western         ar      nohelp  ctl     \
as      nohelp  western         bg      help    western \
bn      help    western         ca      help    western \
cs      help    western         cy      nohelp  western \
da      help    western         de      help    western \
dz      help    ctl             el      help    western \
es      help    western         et      help    western \
eu      help    western         fa      nohelp  ctl     \
fi      help    western         fr      help    western \
ga      nohelp  western         gl      help    western \
gu      nohelp  ctl             he      nohelp  ctl     \
hi      help    ctl             hr      nohelp  western \
hu      help    western         it      help    western \
ja      help    cjk             ko      help    cjk     \
kn      nohelp  western         lt      nohelp  western \
lv      nohelp  western         mai     nohelp  western \
ml      nohelp  western         mr      nohelp  western \
nb      help    western         nl      help    western \
nn      help    western         nr      nohelp  western \
nso     nohelp  western         or      nohelp  ctl     \
pa-IN   nohelp  ctl             pl      help    western \
pt      help    western         pt-BR   help    western \
ro      nohelp  western         ru      help    western \
sh      nohelp  western         si      help    ctl     \
sk      help    western         sl      help    western \
sr      nohelp  western         ss      nohelp  western \
st      nohelp  western         sv      help    western \
ta      nohelp  ctl             te      nohelp  western \
th      nohelp  ctlseqcheck     tn      nohelp  western \
tr      help    western         ts      nohelp  western \
uk      help    western         ve      nohelp  western \
xh      nohelp  western         zh-CN   help    cjk     \
zh-TW   help    cjk             zu      nohelp  western \
)

tar xzf %{SOURCE21}

i=0
while [ $i -lt ${#langpackdetails[@]} ]; do
   lang=${langpackdetails[$i]}
   sed -e "s/LANG/$lang/g" langpacks/libreoffice.langpack-common.template > $lang.filelist
   i=$[i+1]
   help=${langpackdetails[$i]}
   if [ "$help" = "help" ]; then
     sed -e "s/LANG/$lang/g" langpacks/libreoffice.langpack-help.template >> $lang.filelist
   fi
   i=$[i+1]
   type=${langpackdetails[$i]}
   if [ "$type" = "cjk" ]; then
     sed -e "s/LANG/$lang/g" langpacks/libreoffice.langpack-cjk.template >> $lang.filelist
   fi
   #rh217269 upstream made a decision to sequence check all ctl languages
   #I think this is wrong, and only Thai should be sequence checked
   if [ "$type" = "ctlseqcheck" ]; then
     sed -e "s/LANG/$lang/g" langpacks/libreoffice.langpack-ctl.template >> $lang.filelist
   fi
   if [ "$type" = "ctl" ]; then
     rm -f $RPM_BUILD_ROOT/%{basisinstdir}/share/registry/ctl_$lang.xcd
   fi
   i=$[i+1]
done

#rhbz#452379 clump serbian translations together
cat sh.filelist >> sr.filelist

%endif

#remove it in case we didn't build with gcj
rm -f $RPM_BUILD_ROOT/%{basisinstdir}/program/classes/sandbox.jar

#remove dummy .dat files
rm -f $RPM_BUILD_ROOT/%{basisinstdir}/program/root?.dat

#set standard permissions for rpmlint
find $RPM_BUILD_ROOT/%{baseinstdir} -exec chmod +w {} \;
find $RPM_BUILD_ROOT/%{baseinstdir} -type d -exec chmod 0755 {} \;

# move python bits into site-packages
mkdir -p $RPM_BUILD_ROOT/%{python_sitearch}
pushd $RPM_BUILD_ROOT/%{python_sitearch}
echo "import sys, os" > uno.py
echo "sys.path.append('%{basisinstdir}/program')" >> uno.py
echo "os.putenv('URE_BOOTSTRAP', 'vnd.sun.star.pathname:%{baseinstdir}/program/fundamentalrc')" >> uno.py
cat $RPM_BUILD_ROOT/%{basisinstdir}/program/uno.py >> uno.py
rm -f $RPM_BUILD_ROOT/%{basisinstdir}/program/uno.py*
mv -f $RPM_BUILD_ROOT/%{basisinstdir}/program/unohelper.py* .
popd

# rhbz#477435 package opensymbol separately
pushd $RPM_BUILD_ROOT/%{basisinstdir}/share/fonts/truetype
install -d -m 0755 %{buildroot}%{_fontdir}
install -p -m 0644 *.ttf %{buildroot}%{_fontdir}
popd
rm -rf $RPM_BUILD_ROOT/%{basisinstdir}/share/fonts

#ensure that no sneaky un-prelinkable, un-fpic or non executable shared libs 
#have snuck through
pic=0
executable=0
for foo in `find $RPM_BUILD_ROOT/%{instdir} -name "*" -exec file {} \;| grep ": ELF" | cut -d: -f 1` ; do
    chmod +wx $foo
    ls -asl $foo
    result=`readelf -d $foo | grep TEXTREL` || true
    if [ "$result" != "" ]; then
        echo "TEXTREL Warning: $foo is b0rked (-fpic missing)"
        pic=1
    fi
    result=`readelf -l $foo | grep GNU_STACK | grep RWE` || true
    if [ "$result" != "" ]; then
        echo "GNU_STACK Warning: $foo is b0rked (-noexecstack missing)"
        executable=1
    fi
done
if [ $pic == 1 ]; then false; fi
if [ $executable == 1 ]; then false; fi

#make up some /usr/bin scripts
mkdir -p $RPM_BUILD_ROOT/%{_bindir}

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooffice
echo exec libreoffice \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooffice
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooffice

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc
echo exec libreoffice --view \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oowriter
echo exec libreoffice --writer \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oowriter
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oowriter

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oocalc
echo exec libreoffice --calc \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oocalc
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oocalc

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooimpress
echo exec libreoffice --impress \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooimpress
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooimpress

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oodraw
echo exec libreoffice --draw \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oodraw
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oodraw

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oomath
echo exec libreoffice --math \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oomath
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oomath

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oobase
echo exec libreoffice --base \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oobase
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oobase

cp -f %{SOURCE22} $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/LAUNCHER/unopkg/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/BRAND/libreoffice/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/unopkg

cp -f %{SOURCE22} $RPM_BUILD_ROOT/%{_bindir}/libreoffice
sed -i -e "s/LAUNCHER/soffice/g" $RPM_BUILD_ROOT/%{_bindir}/libreoffice
sed -i -e "s/BRAND/libreoffice/g" $RPM_BUILD_ROOT/%{_bindir}/libreoffice
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/libreoffice

pushd $RPM_BUILD_ROOT/%{_bindir}
# rhbz#499474 provide a /usr/bin/soffice for .recently-used.xbel
ln -s %{baseinstdir}/program/soffice soffice
# rhbz#499474 provide a /usr/bin/openoffice.org for backwards compat
ln -s libreoffice openoffice.org
popd

pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/xdg/
chmod u+w *.desktop
rm -rf printeradmin.desktop
ICONVERSION=`echo $PRODUCTVERSION | sed -e 's/\.//'`
for file in *.desktop; do
    # rhbz#156677 remove the version from Name=
    # rhbz#156067 don't version the icons
    sed -i -e "s/ *$PRODUCTVERSION//g" \
        -e "s/$ICONVERSION//g" \
        -e "s/$PRODUCTVERSIONSHORT//g" \
        $file
    # add X-GIO-NoFuse so we get url:// instead of file://~.gvfs/
    echo X-GIO-NoFuse=true >> $file
done
for app in base calc draw impress math writer; do
    echo "StartupNotify=true" >> $app.desktop
    echo "TryExec=oo$app" >> $app.desktop
done
# rhbz#156677# / rhbz#186515#
echo "NoDisplay=true" >> math.desktop
echo "NoDisplay=true" >> startcenter.desktop
# rhbz#491159 temporarily remove NoDisplay=true from qstart.desktop
sed -i -e "/NoDisplay=true/d" qstart.desktop
# relocate the .desktop and icon files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
for app in base calc draw impress javafilter math startcenter writer; do
    desktop-file-validate $app.desktop
    cp -p $app.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-$app.desktop
done
popd

pushd sysui/output/usr/share/
#get rid of the gnome icons and other unneeded files
rm -rf icons/gnome applications application-registry

#relocate the rest of them
for icon in `find icons -type f`; do
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/`dirname $icon`
    cp -p $icon $RPM_BUILD_ROOT/%{_datadir}/`echo $icon | sed -e s@office$ICONVERSION@office@`
done
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime-info
cp -p mime-info/libreoffice$PRODUCTVERSION.keys $RPM_BUILD_ROOT/%{_datadir}/mime-info/libreoffice.keys
cp -p mime-info/libreoffice$PRODUCTVERSION.mime $RPM_BUILD_ROOT/%{_datadir}/mime-info/libreoffice.mime
#add our mime-types, e.g. for .oxt extensions
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime/packages
cp -p mime/packages/libreoffice$PRODUCTVERSION.xml $RPM_BUILD_ROOT/%{_datadir}/mime/packages/libreoffice.xml
popd

rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/readmes
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/licenses

mkdir -p $RPM_BUILD_ROOT/%{basisinstdir}/share/psprint/driver
cp -p psprint_config/configuration/ppds/SGENPRT.PS $RPM_BUILD_ROOT/%{basisinstdir}/share/psprint/driver/SGENPRT.PS

# rhbz#452385 to auto have postgres in classpath if subsequently installed
# rhbz#465664 to get lucene working for functional help
sed -i -e "s#URE_MORE_JAVA_CLASSPATH_URLS.*#& file:///usr/share/java/lucene.jar file:///usr/share/java/lucene-contrib/lucene-analyzers.jar file:///usr/share/java/postgresql-jdbc.jar#" $RPM_BUILD_ROOT/%{basisinstdir}/program/fundamentalbasisrc

export DESTDIR=$RPM_BUILD_ROOT
install-gdb-printers -a %{_datadir}/gdb/auto-load%{baseinstdir} -c -p %{_datadir}/libreoffice/gdb
# fix arch-dependent library suffix
cd solenv/gdb
cat <<EOF > dllpostfix.mk
PRJ=..
.INCLUDE : settings.mk
print-DLLPOSTFIX :
    @echo \$(DLLPOSTFIX)
EOF
libsuffix=`dmake -f dllpostfix.mk print-DLLPOSTFIX`
for f in `find $RPM_BUILD_ROOT/%{_datadir}/gdb/auto-load%{baseinstdir} -type f -name '*lo-gdb.py'`; do
    mv "$f" "${f%lo-gdb.py}${libsuffix}-gdb.py"
done

%check
source ./Linux*Env.Set.sh
cd test
build && deliver -link
cd ../smoketestdoc
build && deliver -link
cd ../smoketestoo_native
unset WITH_LANG
#JFW_PLUGIN_DO_NOT_CHECK_ACCESSIBILITY="1" works around flawed accessibility check
#SAL_USE_VCLPLUGIN="svp" uses the headless plugin for these tests
%if %{defined rhel} && 0%{?rhel} < 7
unset SOLAR_JAVA
JFW_PLUGIN_DO_NOT_CHECK_ACCESSIBILITY="1" SAL_USE_VCLPLUGIN="svp" timeout 2h build.pl
%else
JFW_PLUGIN_DO_NOT_CHECK_ACCESSIBILITY="1" SAL_USE_VCLPLUGIN="svp" timeout -k 2m 2h build.pl
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%files core
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/help
%docdir %{basisinstdir}/help/en
%dir %{basisinstdir}/help/en
%{basisinstdir}/help/en/default.css
%{basisinstdir}/help/en/err.html
%{basisinstdir}/help/en/highcontrast1.css
%{basisinstdir}/help/en/highcontrast2.css
%{basisinstdir}/help/en/highcontrastblack.css
%{basisinstdir}/help/en/highcontrastwhite.css
%{basisinstdir}/help/en/sbasic.*
%{basisinstdir}/help/en/schart.*
%{basisinstdir}/help/en/shared.*
%{basisinstdir}/help/idxcaption.xsl
%{basisinstdir}/help/idxcontent.xsl
%{basisinstdir}/help/main_transform.xsl
%{basisinstdir}/presets
%dir %{basisinstdir}/program
%{basisinstdir}/program/addin
%{basisinstdir}/program/basprov%{SOPOST}.uno.so
%{basisinstdir}/program/canvasfactory.uno.so
%{basisinstdir}/program/cde-open-url
%dir %{basisinstdir}/program/classes
%{basisinstdir}/program/classes/agenda.jar                
%{basisinstdir}/program/classes/commonwizards.jar
%{basisinstdir}/program/classes/fax.jar
%{basisinstdir}/program/classes/form.jar
%{basisinstdir}/program/classes/query.jar          
%{basisinstdir}/program/classes/letter.jar          
%{basisinstdir}/program/classes/LuceneHelpWrapper.jar
%{basisinstdir}/program/classes/officebean.jar
%{basisinstdir}/program/classes/report.jar
%{basisinstdir}/program/classes/saxon9.jar
%{basisinstdir}/program/classes/ScriptFramework.jar
%{basisinstdir}/program/classes/ScriptProviderForJava.jar
%{basisinstdir}/program/classes/table.jar
%{basisinstdir}/program/classes/unoil.jar
%{basisinstdir}/program/classes/web.jar
%{basisinstdir}/program/classes/XMergeBridge.jar
%{basisinstdir}/program/classes/xmerge.jar
%{basisinstdir}/program/classes/XSLTFilter.jar
%{basisinstdir}/program/classes/XSLTValidate.jar
%{basisinstdir}/program/cmdmail.uno.so
%{basisinstdir}/program/deployment%{SOPOST}.uno.so
%{basisinstdir}/program/deploymentgui%{SOPOST}.uno.so
%{basisinstdir}/program/dlgprov%{SOPOST}.uno.so
%{basisinstdir}/program/fastsax.uno.so
%{basisinstdir}/program/fpicker.uno.so
%{basisinstdir}/program/fps_gnome.uno.so
%{basisinstdir}/program/fps_office.uno.so
%{basisinstdir}/program/fundamentalbasisrc
%{basisinstdir}/program/gnome-open-url
%{basisinstdir}/program/gnome-open-url.bin
%{basisinstdir}/program/hatchwindowfactory.uno.so
%{basisinstdir}/program/i18nsearch.uno.so
%{basisinstdir}/program/kde-open-url
%{basisinstdir}/program/legacy_binfilters.rdb
%{basisinstdir}/program/libacc%{SOPOST}.so
%{basisinstdir}/program/libadabas%{SOPOST}.so
%{basisinstdir}/program/libavmedia*.so
%{basisinstdir}/program/libbasctl%{SOPOST}.so
%{basisinstdir}/program/libbf_sb%{SOPOST}.so
%{basisinstdir}/program/libbf_frm%{SOPOST}.so
%{basisinstdir}/program/libbf_go%{SOPOST}.so
%{basisinstdir}/program/libbf_migratefilter%{SOPOST}.so
%{basisinstdir}/program/libbf_ofa%{SOPOST}.so
%{basisinstdir}/program/libbf_sch%{SOPOST}.so
%{basisinstdir}/program/libbf_sd%{SOPOST}.so
%{basisinstdir}/program/libbf_so%{SOPOST}.so
%{basisinstdir}/program/libbf_svt%{SOPOST}.so
%{basisinstdir}/program/libbf_svx%{SOPOST}.so
%{basisinstdir}/program/libbf_wrapper%{SOPOST}.so
%{basisinstdir}/program/libbf_xo%{SOPOST}.so
%{basisinstdir}/program/libbib%{SOPOST}.so
%{basisinstdir}/program/libbindet%{SOPOST}.so
%{basisinstdir}/program/libcached1.so
%{basisinstdir}/program/libcanvastools%{SOPOST}.so
%{basisinstdir}/program/libchart*%{SOPOST}.so
%{basisinstdir}/program/libcollator_data.so
%{basisinstdir}/program/libcppcanvas%{SOPOST}.so
%{basisinstdir}/program/libctl%{SOPOST}.so
%{basisinstdir}/program/libcui%{SOPOST}.so
%{basisinstdir}/program/libdba%{SOPOST}.so
%{basisinstdir}/program/libdbase%{SOPOST}.so
%{basisinstdir}/program/libdbaxml%{SOPOST}.so
%{basisinstdir}/program/libdbmm%{SOPOST}.so
%{basisinstdir}/program/libdbpool2.so
%{basisinstdir}/program/libdbtools%{SOPOST}.so
%{basisinstdir}/program/libdbu%{SOPOST}.so
%{basisinstdir}/program/libdeploymentmisc%{SOPOST}.so
%{basisinstdir}/program/libdesktop_detector%{SOPOST}.so
%{basisinstdir}/program/libdict_ja.so
%{basisinstdir}/program/libdict_zh.so
%{basisinstdir}/program/libdrawinglayer%{SOPOST}.so
%{basisinstdir}/program/libediteng%{SOPOST}.so
%{basisinstdir}/program/libembobj.so
%{basisinstdir}/program/libemboleobj.so
%{basisinstdir}/program/libevoab*.so
%{basisinstdir}/program/libevtatt.so
%{basisinstdir}/program/libegi%{SOPOST}.so    
%{basisinstdir}/program/libeme%{SOPOST}.so
%{basisinstdir}/program/libepb%{SOPOST}.so
%{basisinstdir}/program/libepg%{SOPOST}.so    
%{basisinstdir}/program/libepp%{SOPOST}.so
%{basisinstdir}/program/libeps%{SOPOST}.so    
%{basisinstdir}/program/libept%{SOPOST}.so
%{basisinstdir}/program/libera%{SOPOST}.so    
%{basisinstdir}/program/libeti%{SOPOST}.so
%{basisinstdir}/program/libexp%{SOPOST}.so    
%{basisinstdir}/program/libicd%{SOPOST}.so
%{basisinstdir}/program/libicg%{SOPOST}.so
%{basisinstdir}/program/libidx%{SOPOST}.so
%{basisinstdir}/program/libime%{SOPOST}.so
%{basisinstdir}/program/libindex_data.so
%{basisinstdir}/program/libipb%{SOPOST}.so
%{basisinstdir}/program/libipd%{SOPOST}.so
%{basisinstdir}/program/libips%{SOPOST}.so
%{basisinstdir}/program/libipt%{SOPOST}.so
%{basisinstdir}/program/libipx%{SOPOST}.so
%{basisinstdir}/program/libira%{SOPOST}.so
%{basisinstdir}/program/libitg%{SOPOST}.so
%{basisinstdir}/program/libiti%{SOPOST}.so
%{basisinstdir}/program/libofficebean.so
%{basisinstdir}/program/liboooimprovecore%{SOPOST}.so
%{basisinstdir}/program/libfile%{SOPOST}.so
%{basisinstdir}/program/libfilterconfig1.so
%{basisinstdir}/program/libflat%{SOPOST}.so
%{basisinstdir}/program/libfrm%{SOPOST}.so
%{basisinstdir}/program/libguesslang%{SOPOST}.so
%{basisinstdir}/program/libhelplinker%{SOPOST}.so
%{basisinstdir}/program/libhyphen%{SOPOST}.so
%{basisinstdir}/program/libi18nregexpgcc3.so
%{basisinstdir}/program/libjdbc%{SOPOST}.so
%{basisinstdir}/program/liblegacy_binfilters%{SOPOST}.so
%{basisinstdir}/program/liblng%{SOPOST}.so
%{basisinstdir}/program/liblog%{SOPOST}.so
%{basisinstdir}/program/liblocaledata_en.so
%{basisinstdir}/program/liblocaledata_es.so
%{basisinstdir}/program/liblocaledata_euro.so
%{basisinstdir}/program/liblocaledata_others.so
%{basisinstdir}/program/libmcnttype.so
%{basisinstdir}/program/libmozbootstrap.so
%{basisinstdir}/program/libmsfilter%{SOPOST}.so
%{basisinstdir}/program/libmtfrenderer.uno.so
%{basisinstdir}/program/libmysql%{SOPOST}.so
%{basisinstdir}/program/libodbc%{SOPOST}.so
%{basisinstdir}/program/libodbcbase%{SOPOST}.so
%{basisinstdir}/program/liboffacc%{SOPOST}.so
%{basisinstdir}/program/liboox%{SOPOST}.so
%{basisinstdir}/program/libpcr%{SOPOST}.so
%{basisinstdir}/program/libpdffilter%{SOPOST}.so
%{basisinstdir}/program/libpl%{SOPOST}.so
%{basisinstdir}/program/libpreload%{SOPOST}.so
%{basisinstdir}/program/libprotocolhandler%{SOPOST}.so
%{basisinstdir}/program/libqstart_gtk%{SOPOST}.so
%{basisinstdir}/program/librecentfile.so
%{basisinstdir}/program/libres%{SOPOST}.so
%{basisinstdir}/program/libsax%{SOPOST}.so
%{basisinstdir}/program/libscn%{SOPOST}.so
%{basisinstdir}/program/libscriptframe.so
%{basisinstdir}/program/libsd%{SOPOST}.so
%{basisinstdir}/program/libsdfilt%{SOPOST}.so
%{basisinstdir}/program/libsdbc2.so
%{basisinstdir}/program/libsdbt%{SOPOST}so
%{basisinstdir}/program/libsdd%{SOPOST}.so
%{basisinstdir}/program/libsdui%{SOPOST}.so
%{basisinstdir}/program/libspa%{SOPOST}.so
%{basisinstdir}/program/libspell%{SOPOST}.so
%{basisinstdir}/program/libsrtrs1.so
%{basisinstdir}/program/libsts%{SOPOST}.so
%{basisinstdir}/program/libsvx%{SOPOST}.so
%{basisinstdir}/program/libsvxcore%{SOPOST}.so
%{basisinstdir}/program/libsw%{SOPOST}.so
%{basisinstdir}/program/libtextconv_dict.so
%{basisinstdir}/program/libtextconversiondlgs%{SOPOST}.so
%{basisinstdir}/program/libtvhlp1.so
%{basisinstdir}/program/libodfflatxml%{SOPOST}.so
%{basisinstdir}/program/libucbhelper4gcc3.so
%{basisinstdir}/program/libucpchelp1.so
%{basisinstdir}/program/libucpdav1.so
%{basisinstdir}/program/libucpftp1.so
%{basisinstdir}/program/libucphier1.so
%{basisinstdir}/program/libucppkg1.so
%{basisinstdir}/program/libunordf%{SOPOST}.so
%{basisinstdir}/program/libunopkgapp.so
%{basisinstdir}/program/libunoxml%{SOPOST}.so
%{basisinstdir}/program/libupdchk%{SOPOST}.so
%{basisinstdir}/program/libuui%{SOPOST}.so
%{basisinstdir}/program/libvbahelper%{SOPOST}.so
%{basisinstdir}/program/libvclplug_gen%{SOPOST}.so
%{basisinstdir}/program/libvclplug_gtk%{SOPOST}.so
%if %{undefined rhel} || 0%{?rhel} >= 7
%{basisinstdir}/program/libwpgimport%{SOPOST}.so
%endif
%{basisinstdir}/program/libxmlfa%{SOPOST}.so
%{basisinstdir}/program/libxmlfd%{SOPOST}.so
%{basisinstdir}/program/libxmx%{SOPOST}.so
%{basisinstdir}/program/libxof%{SOPOST}.so
%{basisinstdir}/program/libxsec_fw.so
%{basisinstdir}/program/libxsec_xmlsec.so
%{basisinstdir}/program/libxsltdlg%{SOPOST}.so
%{basisinstdir}/program/libxsltfilter%{SOPOST}.so
%{basisinstdir}/program/libxstor.so
%{basisinstdir}/program/migrationoo2.uno.so
%{basisinstdir}/program/migrationoo3.uno.so
%{basisinstdir}/program/msforms.uno.so
%{basisinstdir}/program/nsplugin
%{basisinstdir}/program/open-url
%{basisinstdir}/program/offapi.rdb
%{basisinstdir}/program/passwordcontainer.uno.so
%{basisinstdir}/program/pagein
%{basisinstdir}/program/pagein-common
%{basisinstdir}/program/plugin
%{basisinstdir}/program/pluginapp.bin
%{basisinstdir}/program/productregistration.uno.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/avmediaen-US.res
%{basisinstdir}/program/resource/accen-US.res
%{basisinstdir}/program/resource/basctlen-US.res
%{basisinstdir}/program/resource/bf_frmen-US.res
%{basisinstdir}/program/resource/bf_ofaen-US.res
%{basisinstdir}/program/resource/bf_schen-US.res
%{basisinstdir}/program/resource/bf_sden-US.res
%{basisinstdir}/program/resource/bf_svten-US.res
%{basisinstdir}/program/resource/bf_svxen-US.res
%{basisinstdir}/program/resource/biben-US.res
%{basisinstdir}/program/resource/calen-US.res
%{basisinstdir}/program/resource/chartcontrolleren-US.res
%{basisinstdir}/program/resource/cuien-US.res
%{basisinstdir}/program/resource/dbaen-US.res
%{basisinstdir}/program/resource/dbmmen-US.res
%{basisinstdir}/program/resource/dbuen-US.res
%{basisinstdir}/program/resource/dbwen-US.res
%{basisinstdir}/program/resource/deploymenten-US.res
%{basisinstdir}/program/resource/deploymentguien-US.res
%{basisinstdir}/program/resource/dkten-US.res
%{basisinstdir}/program/resource/editengen-US.res
%{basisinstdir}/program/resource/epsen-US.res
%{basisinstdir}/program/resource/euren-US.res
%{basisinstdir}/program/resource/fps_officeen-US.res
%{basisinstdir}/program/resource/frmen-US.res
%{basisinstdir}/program/resource/fween-US.res
%{basisinstdir}/program/resource/galen-US.res
%{basisinstdir}/program/resource/impen-US.res
%{basisinstdir}/program/resource/ofaen-US.res
%{basisinstdir}/program/resource/pcren-US.res
%{basisinstdir}/program/resource/pdffilteren-US.res
%{basisinstdir}/program/resource/preloaden-US.res
%{basisinstdir}/program/resource/productregistrationen-US.res
%{basisinstdir}/program/resource/sanen-US.res
%{basisinstdir}/program/resource/sben-US.res
%{basisinstdir}/program/resource/sden-US.res
%{basisinstdir}/program/resource/sfxen-US.res
%{basisinstdir}/program/resource/spaen-US.res
%{basisinstdir}/program/resource/sdbten-US.res
%{basisinstdir}/program/resource/svlen-US.res
%{basisinstdir}/program/resource/svten-US.res
%{basisinstdir}/program/resource/svxen-US.res
%{basisinstdir}/program/resource/swen-US.res
%{basisinstdir}/program/resource/textconversiondlgsen-US.res
%{basisinstdir}/program/resource/tken-US.res
%{basisinstdir}/program/resource/tplen-US.res
%{basisinstdir}/program/resource/uuien-US.res
%{basisinstdir}/program/resource/updchken-US.res
%{basisinstdir}/program/resource/upden-US.res
%{basisinstdir}/program/resource/vclen-US.res
%{basisinstdir}/program/resource/wzien-US.res
%{basisinstdir}/program/resource/xmlsecen-US.res
%{basisinstdir}/program/resource/xsltdlgen-US.res
%{basisinstdir}/program/sax.uno.so
%{basisinstdir}/program/senddoc
%{basisinstdir}/program/services.rdb
%{basisinstdir}/program/simplecanvas.uno.so
%{basisinstdir}/program/slideshow.uno.so
%{basisinstdir}/program/libsofficeapp.so
%{basisinstdir}/program/spadmin.bin
%{basisinstdir}/program/stringresource%{SOPOST}.uno.so
%{basisinstdir}/program/syssh.uno.so
%{basisinstdir}/program/ucpexpand1.uno.so
%{basisinstdir}/program/ucpext.uno.so
%{basisinstdir}/program/ucptdoc1.uno.so
%{basisinstdir}/program/unorc
%{basisinstdir}/program/updatefeed.uno.so
%{basisinstdir}/ure-link
%{basisinstdir}/program/uri-encode
%{basisinstdir}/program/vbaevents%{SOPOST}.uno.so
%{basisinstdir}/program/vclcanvas.uno.so
%{basisinstdir}/program/versionrc
%{basisinstdir}/program/cairocanvas.uno.so
%dir %{basisinstdir}/share
%dir %{basisinstdir}/share/Scripts
%{basisinstdir}/share/Scripts/java
%{basisinstdir}/share/autotext
%{basisinstdir}/share/basic
%dir %{basisinstdir}/share/config
%{basisinstdir}/share/config/images.zip
%{basisinstdir}/share/config/images_crystal.zip
%{basisinstdir}/share/config/images_hicontrast.zip
%{basisinstdir}/share/config/images_oxygen.zip
%{basisinstdir}/share/config/images_tango.zip
%{basisinstdir}/share/config/javasettingsunopkginstall.xml
%{basisinstdir}/share/config/psetup.xpm
%{basisinstdir}/share/config/psetupl.xpm
%dir %{basisinstdir}/share/config/soffice.cfg
%{basisinstdir}/share/config/soffice.cfg/modules
%{basisinstdir}/share/config/symbol
%{basisinstdir}/share/config/webcast
%{basisinstdir}/share/config/wizard
%dir %{basisinstdir}/share/dtd
%{basisinstdir}/share/dtd/officedocument
%{basisinstdir}/share/gallery
%dir %{basisinstdir}/share/psprint
%config %{basisinstdir}/share/psprint/psprint.conf
%{basisinstdir}/share/psprint/driver
%dir %{basisinstdir}/share/registry
%{basisinstdir}/share/registry/binfilter.xcd
%{basisinstdir}/share/registry/gnome.xcd
%{basisinstdir}/share/registry/lingucomponent.xcd
%{basisinstdir}/share/registry/main.xcd
%{basisinstdir}/share/registry/oo-ad-ldap.xcd.sample
%{basisinstdir}/share/registry/oo-ldap.xcd.sample
%{basisinstdir}/share/registry/Langpack-en-US.xcd
%dir %{basisinstdir}/share/registry/res
%{basisinstdir}/share/registry/res/fcfg_langpack_en-US.xcd
%dir %{basisinstdir}/share/samples
%{basisinstdir}/share/samples/en-US
%dir %{basisinstdir}/share/template
%{basisinstdir}/share/template/en-US
%dir %{basisinstdir}/share/template/common
%{basisinstdir}/share/template/common/layout
%{basisinstdir}/share/template/wizard
%dir %{basisinstdir}/share/wordbook
%{basisinstdir}/share/wordbook/en-US
%dir %{basisinstdir}/share/xslt
%{basisinstdir}/share/xslt/common
%dir %{basisinstdir}/share/xslt/export
%{basisinstdir}/share/xslt/export/common
%{basisinstdir}/share/xslt/export/spreadsheetml
%{basisinstdir}/share/xslt/export/wordml
%dir %{basisinstdir}/share/xslt/import
%{basisinstdir}/share/xslt/import/common
%{basisinstdir}/share/xslt/import/spreadsheetml
%{basisinstdir}/share/xslt/import/wordml
%{basisinstdir}/program/liblnth%{SOPOST}.so
%{_bindir}/unopkg
#icons and mime
%{_datadir}/icons/*/*/*/libreoffice*
%{_datadir}/mime-info/libreoffice.*
%{basisinstdir}/program/libxmlsecurity.so
%{_datadir}/mime/packages/libreoffice.xml
%{basisinstdir}/program/configmgr.uno.so
%{basisinstdir}/program/desktopbe1.uno.so
%{basisinstdir}/program/fsstorage.uno.so
%{basisinstdir}/program/gconfbe1.uno.so
%{basisinstdir}/program/i18npool.uno.so
%{basisinstdir}/program/libbasegfx%{SOPOST}.so
%{basisinstdir}/program/libcomphelpgcc3.so
%{basisinstdir}/program/libfileacc.so
%{basisinstdir}/program/libfwe%{SOPOST}.so
%{basisinstdir}/program/libfwi%{SOPOST}.so
%{basisinstdir}/program/libfwk%{SOPOST}.so
%{basisinstdir}/program/libfwl%{SOPOST}.so
%{basisinstdir}/program/libfwm%{SOPOST}.so
%{basisinstdir}/program/libi18nisolang*.so
%{basisinstdir}/program/libi18npaper*.so
%{basisinstdir}/program/libi18nutilgcc3.so
%{basisinstdir}/program/libpackage2.so
%{basisinstdir}/program/libsb%{SOPOST}.so
%{basisinstdir}/program/libsfx%{SOPOST}.so
%{basisinstdir}/program/libsot%{SOPOST}.so
%{basisinstdir}/program/libspl%{SOPOST}.so
%{basisinstdir}/program/libspl_unx%{SOPOST}.so
%{basisinstdir}/program/libsvl%{SOPOST}.so
%{basisinstdir}/program/libsvt%{SOPOST}.so
%{basisinstdir}/program/libtk%{SOPOST}.so
%{basisinstdir}/program/libtl%{SOPOST}.so
%{basisinstdir}/program/libucb1.so
%{basisinstdir}/program/libucpfile1.so
%{basisinstdir}/program/libutl%{SOPOST}.so
%{basisinstdir}/program/libvcl%{SOPOST}.so
%{basisinstdir}/program/libxcr%{SOPOST}.so
%{basisinstdir}/program/libxo%{SOPOST}.so
%{basisinstdir}/program/localebe1.uno.so
%{basisinstdir}/program/ucpgio1.uno.so
%{basisinstdir}/program/oovbaapi.rdb
#share unopkg
%dir %{baseinstdir}
%{baseinstdir}/basis-link
%dir %{baseinstdir}/share
%dir %{baseinstdir}/share/extensions
%{baseinstdir}/share/extensions/package.txt
%dir %{baseinstdir}/program
%{baseinstdir}/program/unopkg
%{baseinstdir}/program/unopkg.bin
%{baseinstdir}/program/bootstraprc
%{baseinstdir}/program/fundamentalrc
%{baseinstdir}/program/setuprc
%{baseinstdir}/program/services.rdb
%{baseinstdir}/program/versionrc
%doc %{baseinstdir}/CREDITS.odt
%doc %{baseinstdir}/LICENSE
%doc %{baseinstdir}/LICENSE.odt
%doc %{baseinstdir}/THIRDPARTYLICENSEREADME.html
%{baseinstdir}/program/about.*
%{baseinstdir}/program/intro.*
%{baseinstdir}/program/soffice
%{baseinstdir}/program/soffice.bin
%{baseinstdir}/program/sofficerc
%{baseinstdir}/program/spadmin
%{baseinstdir}/program/unoinfo
%{baseinstdir}/program/libnpsoplugin.so
%{baseinstdir}/program/oosplash.bin
%{baseinstdir}/program/shell/
%dir %{baseinstdir}/share/config
%{baseinstdir}/share/config/images_brand.zip
%dir %{baseinstdir}/share/registry
%{baseinstdir}/share/registry/brand.xcd
%{baseinstdir}/share/xdg/
%{baseinstdir}/program/redirectrc
%{_datadir}/applications/libreoffice-startcenter.desktop
#launchers
%{_bindir}/libreoffice
%{_bindir}/openoffice.org
%{_bindir}/soffice
%{_bindir}/ooffice
%{_bindir}/ooviewdoc

%post core
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :
for theme in hicolor locolor; do
    touch --no-create %{_datadir}/icons/$theme &>/dev/null || :
done

%postun core
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ $1 -eq 0 ] ; then
    for theme in hicolor locolor; do
        touch --no-create %{_datadir}/icons/$theme &>/dev/null || :
        gtk-update-icon-cache -q %{_datadir}/icons/$theme &>/dev/null || :
    done
fi

%posttrans core
for theme in hicolor locolor; do
    gtk-update-icon-cache -q %{_datadir}/icons/$theme &>/dev/null || :
done


%files base
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/sdatabase.*
%dir %{basisinstdir}/program
%dir %{basisinstdir}/program/classes
%if %{undefined rhel} || 0%{?rhel} >= 7
%{basisinstdir}/program/classes/hsqldb.jar
%endif
%{basisinstdir}/program/classes/sdbc_hsqldb.jar
%{basisinstdir}/program/libabp%{SOPOST}.so
%{basisinstdir}/program/libadabasui%{SOPOST}.so
%{basisinstdir}/program/libdbp%{SOPOST}.so
%{basisinstdir}/program/libhsqldb.so
%{basisinstdir}/program/librpt*%{SOPOST}.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/abpen-US.res
%{basisinstdir}/program/resource/adabasuien-US.res
%{basisinstdir}/program/resource/cnren-US.res
%{basisinstdir}/program/resource/dbpen-US.res
%{basisinstdir}/program/resource/rpten-US.res
%{basisinstdir}/program/resource/rptuien-US.res
%{basisinstdir}/program/resource/sdbclen-US.res
%{basisinstdir}/program/resource/sdberren-US.res
%{basisinstdir}/share/registry/base.xcd
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/sbase
%{_datadir}/applications/libreoffice-base.desktop
%{_bindir}/oobase

%post base
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun base
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files report-builder
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/report-builder/help
%{baseinstdir}/share/extensions/report-builder

%files bsh
%defattr(-,root,root,-)
%{basisinstdir}/share/Scripts/beanshell
%{baseinstdir}/share/extensions/script-provider-for-beanshell

%files rhino
%defattr(-,root,root,-)
%{basisinstdir}/share/Scripts/javascript
%{baseinstdir}/share/extensions/script-provider-for-javascript

%files wiki-publisher
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/wiki-publisher/license
%{baseinstdir}/share/extensions/wiki-publisher

%files ogltrans
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/OGLTrans.uno.so
%dir %{basisinstdir}/share/config
%dir %{basisinstdir}/share/config/soffice.cfg
%dir %{basisinstdir}/share/config/soffice.cfg/simpress
%{basisinstdir}/share/config/soffice.cfg/simpress/transitions-ogl.xml
%{basisinstdir}/share/registry/ogltrans.xcd

%files presentation-minimizer
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/presentation-minimizer/help
%{baseinstdir}/share/extensions/presentation-minimizer

%files presenter-screen
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/presenter-screen/help
%{baseinstdir}/share/extensions/presenter-screen

%files pdfimport
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/pdfimport/help
%{baseinstdir}/share/extensions/pdfimport

%_font_pkg -n %{fontname} opens___.ttf
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_fontdir}

%files calc
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/scalc.*
%dir %{basisinstdir}/program
%{basisinstdir}/program/libanalysis%{SOPOST}.so
%{basisinstdir}/program/libbf_sc%{SOPOST}.so
%{basisinstdir}/program/libcalc%{SOPOST}.so
%{basisinstdir}/program/libdate%{SOPOST}.so
%{basisinstdir}/program/libfor%{SOPOST}.so
%{basisinstdir}/program/libforui%{SOPOST}.so
%{basisinstdir}/program/libsc%{SOPOST}.so
%{basisinstdir}/program/libscd%{SOPOST}.so
%{basisinstdir}/program/libscfilt%{SOPOST}.so
%{basisinstdir}/program/libscui%{SOPOST}.so
%{basisinstdir}/program/libsolver%{SOPOST}.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/analysisen-US.res
%{basisinstdir}/program/resource/bf_scen-US.res
%{basisinstdir}/program/resource/dateen-US.res
%{basisinstdir}/program/resource/foren-US.res
%{basisinstdir}/program/resource/foruien-US.res
%{basisinstdir}/program/resource/scen-US.res
%{basisinstdir}/program/resource/solveren-US.res
%{basisinstdir}/program/vbaobj.uno.so
%{basisinstdir}/share/registry/calc.xcd
%{basisinstdir}/program/pagein-calc
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/scalc
%{_datadir}/applications/libreoffice-calc.desktop
%{_bindir}/oocalc

%post calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files draw
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/sdraw.*
%{basisinstdir}/share/registry/draw.xcd
%{basisinstdir}/program/pagein-draw
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/sdraw
%{_datadir}/applications/libreoffice-draw.desktop
%{_bindir}/oodraw

%post draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files emailmerge
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/mailmerge.py*

%files writer
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/swriter.*
%dir %{basisinstdir}/program
%{basisinstdir}/program/libbf_sw%{SOPOST}.so
%{basisinstdir}/program/libhwp.so
%{basisinstdir}/program/liblwpft%{SOPOST}.so
%{basisinstdir}/program/libmsword%{SOPOST}.so
%if %{undefined rhel} || 0%{?rhel} >= 7
%{basisinstdir}/program/libmsworks%{SOPOST}.so
%endif
%{basisinstdir}/program/libswd%{SOPOST}.so
%{basisinstdir}/program/libswui%{SOPOST}.so
%{basisinstdir}/program/libt602filter%{SOPOST}.so
%{basisinstdir}/program/libwpft%{SOPOST}.so
%{basisinstdir}/program/libwriterfilter%{SOPOST}.so
%{basisinstdir}/program/vbaswobj.uno.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/bf_swen-US.res
%{basisinstdir}/program/resource/t602filteren-US.res
%{basisinstdir}/share/registry/writer.xcd
%{basisinstdir}/program/pagein-writer
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/swriter
%{_datadir}/applications/libreoffice-writer.desktop
%{_bindir}/oowriter

%post writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files impress
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/simpress.*
%dir %{basisinstdir}/program
%{basisinstdir}/program/libanimcore.so
%{basisinstdir}/program/libplaceware*.so
%dir %{basisinstdir}/share/config
%dir %{basisinstdir}/share/config/soffice.cfg
%dir %{basisinstdir}/share/config/soffice.cfg/simpress
%{basisinstdir}/share/config/soffice.cfg/simpress/effects.xml
%{basisinstdir}/share/config/soffice.cfg/simpress/transitions.xml
%{basisinstdir}/share/registry/impress.xcd
%{basisinstdir}/program/pagein-impress
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/simpress
%{_datadir}/applications/libreoffice-impress.desktop
%{_bindir}/ooimpress

%post impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files math
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/smath.*
%dir %{basisinstdir}/program
%{basisinstdir}/program/libbf_sm%{SOPOST}.so
%{basisinstdir}/program/libsm%{SOPOST}.so
%{basisinstdir}/program/libsmd%{SOPOST}.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/bf_smen-US.res
%{basisinstdir}/program/resource/smen-US.res
%{basisinstdir}/share/registry/math.xcd
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/smath
%{_datadir}/applications/libreoffice-math.desktop
%{_bindir}/oomath

%post math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files graphicfilter
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/libflash%{SOPOST}.so
%{basisinstdir}/program/libsvgfilter%{SOPOST}.so
%{basisinstdir}/share/registry/graphicfilter.xcd

%files xsltfilter
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/share/xslt
%{basisinstdir}/share/xslt/docbook
%dir %{basisinstdir}/share/xslt/export
%{basisinstdir}/share/xslt/export/uof
%{basisinstdir}/share/xslt/export/xhtml
%dir %{basisinstdir}/share/xslt/import
%{basisinstdir}/share/xslt/import/uof
%{basisinstdir}/share/registry/xsltfilter.xcd

%files javafilter
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%dir %{basisinstdir}/program/classes
%{basisinstdir}/program/classes/aportisdoc.jar
%{basisinstdir}/program/classes/pexcel.jar
%{basisinstdir}/program/classes/pocketword.jar
%{_datadir}/applications/libreoffice-javafilter.desktop
%{basisinstdir}/share/registry/palm.xcd
%{basisinstdir}/share/registry/pocketexcel.xcd
%{basisinstdir}/share/registry/pocketword.xcd

%files testtools
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/libcommuni%{SOPOST}.so
%{basisinstdir}/program/libsimplecm%{SOPOST}.so
%{basisinstdir}/program/testtoolrc
%{basisinstdir}/program/testtool.bin
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/stten-US.res

%files ure
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{baseinstdir}
%{ureinstdir}

%files sdk
%defattr(-,root,root,-)
%{sdkinstdir}/
%exclude %{sdkinstdir}/docs/
%exclude %{sdkinstdir}/examples/

%files sdk-doc
%defattr(-,root,root,-)
%docdir %{sdkinstdir}/docs
%{sdkinstdir}/docs/
%{sdkinstdir}/examples/

%files headless
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/libbasebmp%{SOPOST}.so
%{basisinstdir}/program/libvclplug_svp%{SOPOST}.so

%files pyuno
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/libpyuno.so
%{basisinstdir}/program/officehelper.py*
%{basisinstdir}/program/pythonloader.py*
%{basisinstdir}/program/pythonloader.uno.so
%{basisinstdir}/program/pythonloader.unorc
%{basisinstdir}/program/pyuno.so
%dir %{basisinstdir}/share/Scripts
%{basisinstdir}/share/Scripts/python
%{python_sitearch}/uno.py*
%{python_sitearch}/unohelper.py*
%{baseinstdir}/share/extensions/script-provider-for-python
%{basisinstdir}/share/registry/pyuno.xcd

%if %{undefined rhel}
%files kde
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/kde4be1.uno.so
%{basisinstdir}/program/fps_kde4.uno.so
%{basisinstdir}/program/libvclplug_kde4%{SOPOST}.so
%endif

%changelog
* Mon Jan 30 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 3.4.5.2-1.R
- rebuilt for EL6

* Tue Jan 17 2012 David Tardon <dtardon@redhat.com> - 3.4.5.2-1
- new upstream version 3.4.5
- drop integrated 001-add-Oracle-Java-1.7.0-recognition.patch
- drop integrated 001-fix-horizontal-scrollbars-with-KDE-oxygen-style-bnc-.patch
- drop integrated 001-fdo-43308-Set-the-logic-straight-for-center-across-s.patch
- drop integrated 001-Resolves-rhbz-754051-Libreoffice-calc-crashes-when-r.patch
- drop integrated 001-sw-fdo-39159-fdo-40482-temp-selection-print-doc.patch
- Resolves: rhbz#771108 English menu in writer despite installation of
  libreoffice-langpack-de
- Resolves: rhbz#661738 Very slow java database operations:
  Attach/DetachCurrentThread
- Resolves: fdo#44078 fix font alias name problems

* Fri Jan 06 2012 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-7
- Resolves: fdo#40482 Writer view options destroyed by printing
- Resolves: rhbz#533318 smath does not handle accents in MathML

* Thu Dec 15 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-6
- Resolves: rhbz#761009 IFSD_Equal is asymmetrical
- Resolves: rhbz#754051 Libreoffice calc crashes when re-opening a xlxs file
- Resolves: rhbz#767708 write to mmap'ed file w/o disk space: SIGBUS

* Fri Dec 09 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-5
- Resolves: rhbz#759647 dispose clears mpPresTimer
- Resolves: rhbz#761558 center-across-selection fix

* Wed Nov 30 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-4
- Resolves: rhbz#757653 fix headless crash with cairo canvas
- Resolves: rhbz#758338 KDE build problems

* Wed Nov 23 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-3
- Resolves: rhbz#751290 kde black on dark-grey tooltip-texts

* Fri Nov 11 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-2
- Resolves: fdo#42749 KDE oxygen theme and scrollbars

* Fri Nov 11 2011 David Tardon <dtardon@redhat.com> - 3.4.4.2-1
- new upstream version 3.4.4

* Thu Nov 10 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-16
- Resolves: rhbz#751982 shadowed m_aXineramaScreenIndexMap crash

* Thu Oct 27 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-15
- Related: rhbz#748585 throw the additional requires away, because it
  does not help
- add possible fix for detection of java 7

* Tue Oct 25 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-14
- Resolves: rhbz#748585 libreoffice installs Java 7

* Fri Oct 21 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-13
- Resolves: rhbz#747356 let Qt call XInitThreads
- fix .sdw import

* Wed Oct 19 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-12
- Related: rhbz#743750 addXineramaScreenUnique issue

* Mon Oct  3 2011 Marek Kasik <mkasik@redhat.com> - 3.4.3.2-11
- Rebuild (poppler-0.18.0 stable)
- Enable pagein (by Caolán McNamara)
- add 0001-fedora-gcc-4.6.1.patch to build with fedora gcc 4.6.1

* Wed Sep 21 2011 Marek Kasik <mkasik@redhat.com> - 3.4.3.2-10
- Rebuild (poppler-0.17.3)

* Tue Sep 20 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-9
- Resolves: rhbz#738133 fix bn discard string
- Resolves: fdo#35513 avoid crash while processing incorrect print range

* Thu Sep 15 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-8
- Resolves: rhbz#738255 avoid crash on sc inputhdl

* Thu Sep 08 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-7
- rebuild for new icu

* Tue Sep 06 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-6
- Resolves: rhbz#734976 libreoffice-langpack-*-* not pulled in by
  yum install libreoffice

* Fri Sep 02 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-5
- Resolves: rhbz#735182 be able to rebuild against poppler 0.17.3

* Tue Aug 30 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-4
- Resolves: rhbz#734432 openoffice.org symlink broken

* Mon Aug 29 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-3
- add Latvian langpack

* Fri Aug 26 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-2
- Resolves: rhbz#733564 graphite2 now packaged into fedora
- Related: fdo#37195 migrationoo3 not registered

* Thu Aug 25 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-1
- 3.4.3 rc2

* Mon Aug 22 2011 David Tardon <dtardon@redhat.com> - 3.4.3.1-2
- add gdb pretty printers

* Tue Aug 16 2011 David Tardon <dtardon@redhat.com> - 3.4.3.1-1
- 3.4.3 rc1
- drop integrated 0001-Resolves-rhbz-725144-wrong-csh-syntax.patch

* Fri Aug 12 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.3-3
- Related: rhbz#730225 avoid segv in ld

* Tue Aug 02 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.3-2
- Resolves: rhbz#693265 fix crash from unhandled exception

* Fri Jul 29 2011 David Tardon <dtardon@redhat.com> - 3.4.2.3-1
- 3.4.2 rc3

* Mon Jul 25 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.2-2
- Resolves: rhbz#725144 wrong csh syntax

* Wed Jul 20 2011 David Tardon <dtardon@redhat.com> - 3.4.2.2-1
- 3.4.2 rc2
- fix breakage in KDE4 plugin

* Tue Jul 19 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.1-3
- Resolves: rhbz#715549 use fontconfig's detected format

* Mon Jul 18 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.1-2
- Rebuild (poppler-0.17.0), add libreoffice-poppler-0.17.0.patch
  seeing as the API changed for some reason or other

* Wed Jul 13 2011 David Tardon <dtardon@redhat.com> - 3.4.2.1-1
- 3.4.2 rc1
- drop 0001-bad-merge-fix-to-enable-extensions-to-build-again.patch
- drop 0001-fix-regression-in-SvGlobalName-operator.patch

* Tue Jul 12 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.3-3
- fix regression in SvGlobalName operator

* Tue Jul 05 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.3-2
- Related: rhbz#718976 crash in SwTxtSizeInfo::GetMultiCreator

* Fri Jul 01 2011 David Tardon <dtardon@redhat.com> - 3.4.1.3-1
- 3.4.1 rc3

* Thu Jun 23 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.2-1
- 3.4.1 rc2
- drop integrated 0001-correctly-build-GTK-systray-icon.patch

* Tue Jun 21 2011 David Tardon <dtardon@redhat.com> - 3.4.1.1-5
- Resolves: rhbz#714781 add Persian langpack
- Resolves: rhbz#667082 do not crash importing section containing just
  an empty paragraph

* Mon Jun 20 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.1-4
- Related: rhbz#711087 band aid for crash in sc undo
- Resolves: rhbz#714338 add a metapackage to install standard bits

* Fri Jun 17 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.1-3
- Related: rhbz#702833 addEventListener without removeEventListener

* Thu Jun 16 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.1-2
- Resolves: rhbz#713154 pdf export dialog too tall to fit

* Wed Jun 15 2011 David Tardon <dtardon@redhat.com> - 3.4.1.1-1
- 3.4.1 RC1
- drop integrated 0001-Resolves-rhbz-707317-avoid-crash-in-getRowSpan.patch
- drop integrated 0001-Resolves-rhbz-710004-band-aid-for-immediate-crash-in.patch
- drop integrated 0001-Resolves-rhbz-710556-don-t-crash-on-missing-graphics.patch
- drop integrated 0001-Resolves-rhbz-699909-crash-in-export-of-.doc-in-lcl_.patch
- drop integrated 0001-fdo-37584-Make-a-real-copy-of-the-text-where-to-coun.patch
- drop integrated 0001-Resolves-fdo-37668-bitwise-operations-on-signed-numb.patch

* Thu Jun 09 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.2-5
- Resolves: rhbz#699909 crash in export of .doc in lcl_getField
- Resolves: fdo#37584 Make a real copy of the text
- Resolves: rhbz#709503/fdo#37668 bitwise operations on signed values

* Tue Jun 07 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.2-4
- Resolves: rhbz#710556 't crash on missing graphics .pptx export
- Resolves: rhbz#652604 better survive exceptions in autorecovery

* Thu Jun 02 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.2-3
- Resolves: rhbz#710004 band aid for crash

* Mon May 30 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.2-2
- Resolves: rhbz#707317 avoid crash in getRowSpan

* Fri May 27 2011 David Tardon <dtardon@redhat.com> - 3.4.0.2-1
- 3.4.0 RC2
- drop integrated 0001-fix-build-with-system-bsh.patch

* Wed May 25 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.1-3
- rebuild for new hunspell

* Tue May 24 2011 David Tardon <dtardon@redhat.com> - 3.4.0.1-2
- Resolves: rhbz#706110 oosplash.bin segfault on every login

* Fri May 20 2011 David Tardon <dtardon@redhat.com> - 3.4.0.1-1
- 3.4 RC1
- Resolves: rhbz#702635 set correct page number when exporting selected
  pages

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 3.3.99.4-2
- Update icon cache scriptlet

* Sat May 07 2011 David Tardon <dtardon@redhat.com> 3.3.99.4-1
- 3.4 beta4
- drop integrated 0001-Removed-duplicate-code-block-mis-merge-prolly.patch
- drop integrated 7de0b88ce2dd932915894385b54be1897d5ee053.zip

* Mon Apr 18 2011 Caolán McNamara <caolanm@redhat.com> 3.3.99.1-2
- Resolves: rhbz#695509 crash in RefreshDocumentLB
- bubble down configure test findings on visibility

* Tue Apr 11 2011 Caolán McNamara <caolanm@redhat.com> 3.3.99.1-1
- 3.4 beta1
- drop openoffice.org-1.9.123.ooo53397.prelinkoptimize.desktop.patch
  in favour of ooosplash
- drop openoffice.org-2.2.0.gccXXXXX.solenv.javaregistration.patch
  because components are passively registered now
- drop integrated openoffice.org-3.1.0.ooo102061.sc.cellanchoring.patch
- drop integrated turn-script-providers-into-extensions.patch
- drop integrated 0001-tidy-this-up-and-don-t-bail-out-on-mislength-records.patch
- drop integrated 0001-free-ctxt-after-taking-lastError-details.patch
- drop integrated 0001-Removed-suspect-hack.-Cursor-on-post-it-now-scrolls-.patch
- drop integrated libreoffice-gcc4.6.0.patch
- drop integrated 0001-fexceptions-fexceptions.patch
- drop integrated 0001-Related-rhbz-672872-cancel-gtk-file-dialog-on-deskto.patch
- drop vbahelper.visibility.patch
- drop integrated 0001-Resolves-fdo-33509-i62414-out-by-one-breaks-CTL-spel.patch
- drop integrated 0001-Resolves-rhbz-670020-crash-in-slidesorting.patch
- drop integrated 0001-Resolves-rhbz-676539-handle-missing-pWindows-from-xW.patch
- drop integrated 0001-Resolves-fdo-33750-i94623-use-optimal-border-width-w.patch
- drop integrated 0001-rhbz-649310-don-t-crash-deregistering-diff.-platform.patch
- drop integrated 0001-Resolves-rhbz-674330-dereference-of-NULL-mpBase.patch
- drop integrated 0001-rhbz-678284-Get-correct-current-position-when-shift-page-up-and-.patch
- drop integrated 0001-Resolves-rhbz-681159-bandaid-for-crash.patch
- drop integrated 0001-Resolves-rhbz-672818-bandaid-for-crash-in-SwTxtNode-.patch
- drop integrated 0001-install-high-resolution-icons.patch
- drop integrated 0001-Resolves-rhbz-682716-pa-IN-isn-t-handled-by-fontconf.patch
- drop integrated 0001-Related-rhbz-684477-make-sure-this-is-thread-safe.patch
- drop integrated 0001-Resolves-rhbz-682621-better-resizing-of-overtall-gly.patch
- drop integrated 0001-Resolves-rhbz-684620-crash-with-NULL-pTableBox.patch
- drop integrated libreoffice-fdo33947.sd.print.crash.patch
- drop integrated 0001-add-cairo_ft_font_face_create_for_pattern-wrapper.patch
- drop integrated 0001-Related-rhbz-680460-reorganize-this-to-make-it-inher.patch
- drop integrated 0001-Related-rhbz-680460-don-t-bother-with-an-interim-Fon.patch
- drop integrated 0001-Resolves-rhbz-680460-honour-lcdfilter-subpixeling-et.patch
- drop integrated 0001-Cut-Gordian-Knot-of-who-owns-the-font-options.patch
- drop integrated 0001-beware-of-invalidated-iterator.patch
- drop integrated rhbz680766.fix-mdds-crash.patch
- drop integrated 0001-Resolves-rhbz-684580-X-and-strike-through-escapes-ra.patch
- drop integrated 0001-set-mime-types-on-flat-xml-filters.patch
- drop integrated 0001-add-flat-xml-types-to-.desktop-files-etc.patch
- drop integrated libreoffice-fdo31271.icu.patch

* Tue Apr 05 2011 Caolán McNamara <caolanm@redhat.com> 3.3.2.2-6
- Resolves: rhbz#655686 get order of shutdown correct

* Wed Mar 30 2011 Caolán McNamara <caolanm@redhat.com> 3.3.2.2-5
- Add application/vnd.oasis.opendocument.text-flat-xml, etc. to
  .desktop files for mcepl

* Tue Mar 29 2011 Caolán McNamara <caolanm@redhat.com> 3.3.2.2-4
- Resolves: rhbz#684580 improve X and / strike-through

* Thu Mar 24 2011 David Tardon <dtardon@redhat.com> 3.3.2.2-3
- Resolves: rhbz#680766 crash in mdds

* Wed Mar 23 2011 David Tardon <dtardon@redhat.com> 3.3.2.2-2
- Related: rhbz#689268 versioned deps need to contain epoch

* Tue Mar 22 2011 Caolán McNamara <caolanm@redhat.com> 3.3.2.2-1
- latest version
- drop integrated 0001-Resolves-fdo-33701-ensure-node-outlives-path.patch
- drop integrated 0001-valgrind-don-t-leave-an-evil-thread-running-after-ma.patch

* Tue Mar 22 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-12
- Fix fontoptions cache
- avoid crash in calc on changing size of rows (dtardon)

* Mon Mar 21 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-11
- Resolves: rhbz#689268 autocorrs from OOo F14 not upgraded

* Wed Mar 16 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-10
- Resolves: rhbz#680460 honour lcdfilter and subpixeling

* Tue Mar 15 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-9
- Resolves: fdo#33947 sd print crash

* Mon Mar 14 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-8
- Related: rhbz#684477 make sure this is thread safe
- Resolves: rhbz#684620 crash with NULL pTableBox

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> 3.3.1.2-7
- Rebuild (poppler-0.16.3)

* Wed Mar 09 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-6
- Resolves: rhbz#682621 better resizing of overtall glyphsubs

* Tue Mar 08 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-5
- Resolves: rhbz#682716 pa-IN isn't handled well by fontconfig

* Tue Mar 08 2011 David Tardon <dtardon@redhat.com> 3.3.1.2-4
- install 128x128 px icons

* Thu Mar 02 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-3
- Resolves: rhbz#681159 crash in writer
- Resolves: rhbz#672818 crash in writer
- Resolves: fdo#33701 ensure node outlives path
- Resolves: rhbz#681738 crash on writing config post-main

* Thu Feb 17 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-2
- Resolves: rhbz#678284 Calc crashes during cell select with keys
  (dtardon)

* Thu Feb 17 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-1
- RC2

* Wed Feb 16 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.1-2
- Resolves: rhbz#674330 dereference of NULL mpBase

* Fri Feb 11 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.1-1
- 3.3.1 rc1
- drop integrated 0001-don-t-pushback-and-process-a-corrupt-extension.patch
- drop integrated libreoffice-fdo32561.comphelper.patch
- drop integrated 0001-Related-rhbz-610103-more-woes-on-rpm-upgrade-vs-rpm-.patch
- drop integrated 0001-Resolves-rhbz-673819-crash-on-changing-position-of-d.patch
- drop integrated 0001-rhbz-666440-don-t-pushback-and-process-a-corrupt-extension.patch

* Thu Feb 10 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
- Related: rhbz#610103 make this even more robust
- Related: rhbz#672872 cancel gtk file dialog on terminate
- Resolves: fdo#33509/ooo#62414 fix CTL spelling popup
- Resolves: rhbz#673819 crash on changing position of header/footer object
- Resolves: rhbz#670020 crash in slidesorting
- Resolves: rhbz#676539 handle missing pWindows from xWindows
- Resolves: rhbz#649310 don't crash deregistering diff. platform ext.
  (dtardon)
- Resolves: rhbz#666440 don't pushback and process a corrupt extension

* Mon Jan 24 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.4-2
- Resolves: rhbz#671540 fix lonely )

* Thu Jan 20 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.4-1
- next release candidate
- drop integrated 0001-fix-presenter-screens-description.xml-build.patch

* Tue Jan 18 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.3-2
- backport fix to get presenter screen working
- make handling busted extensions more robust

* Wed Jan 12 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.3-1
- latest version
- drop integrated 0001-Resoves-rhbz-663857-font-color-missing-C-FAQ-10.3-do.patch
- drop integrated 0001-Avoid-double-paste-when-pasting-text-into-cell-comme.patch
- drop integrated 0001-Resolves-rhbz-660342-Undo-Redo-crash-with-postits.patch
- drop integrated 0001-Resolves-rhbz-666088-clean-up-search-cache-singleton.patch

* Thu Jan 06 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.2-5
- Resolves: rhbz#666088 don't crash on clean up of search cache

* Wed Jan 05 2011 Lukas Tinkl <ltinkl@redhat.com> 3.3.0.2-4
- create a KDE integration subpackage

* Mon Jan 03 2011 David Tardon <dtardon@redhat.com> 3.3.0.2-3
- rebuild with new poppler

* Wed Dec 22 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.2-2
- Resolves: rhbz#663724 fdo32572-sc-dont-double-paste.patch
- Resolves: rhbz#660342 Undo/Redo crash with postits

* Tue Dec 21 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.2-1
- latest version

* Sat Dec 18 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.1-4
- Resolves: rhbz#663857 font color missing in transitions

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.3.0.1-3
- rebuild (poppler)

* Wed Dec 15 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.1-2
- Fix up some doc imports

* Sun Dec 05 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.1-1
- release candidate 1
- drop integrated qstart.dont-forceenabled-on-post-reg-restart.patch
- drop integrated exit.quickstarter.when.deleted.patch
- drop integrated 0001-destroydesktop.in.timeout.patch
- drop integrated openoffice.org-3.3.0.rhbz657541.join-paragraphs.patch

* Sat Nov 27 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.3-2
- Resolves: rhbz#610103 exit quickstarter when libs deleted
- Resolves: rhbz#652695 release desktop in timeout
- Resolves: rhbz#657541 don't crash during processing of auto. styles
  when joining paragraphs (dtardon)

* Thu Nov 18 2010 Caolán McNamara <caolanm@redhat.com 3.2.99.3-1
- next Libreoffice milestone
- drop integrated openoffice.org-2.0.1.rhXXXXXX.extensions.defaulttoevo2.patch
- drop integrated openoffice.org-2.2.1.ooo7065.sw.titlepagedialog.patch
- drop integrated openoffice.org-3.2.0.ooo108846.sfx2.qstartfixes.patch
- drop integrated openoffice.org-3.3.0.ooo107490.cppu.lifecycle.patch
- drop integrated libreoffice-buildfix.patch
- drop integrated libreoffice-xdg632229.gnomeshell.patch
- drop integrated 0001-strcpy-cannot-be-used-with-overlapping-src-and-dest.patch
- drop integrated 0001-abort-doesn-t-gain-us-anything-here.patch
- drop integrated 0001-latest-libX11-changed-header-guards.patch

* Sat Nov 06 2010 David Tardon <dtardon@redhat.com 3.2.99.2-6
- turn script providers into extensions

* Wed Nov 03 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-5
- Resolves: rhbz#649210 add Sinhalese langpack

* Sun Oct 30 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-4
- langpack macro hard-coded version number

* Fri Oct 22 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-3
- Resolves: xdg632229 gnomeshell app tracking

* Tue Oct 12 2010 David Tardon <dtardon@redhat.com> 3.2.99.2-2
- use macros to define auto-correction and language pack subpackages

* Mon Oct 11 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-1
- next LibreOffice milestone
- drop integrated openoffice.org-2.3.0.ooo76649.httpencoding.patch
- drop integrated workspace.dtardon03.patch
- drop integrated openoffice.org-3.1.0.ooo61927.sw.ww6.unicodefontencoding.patch
- drop integrated workspace.impress195.patch
- drop integrated workspace.srb1.patch
- drop integrated openoffice.org-3.2.0.ooo106502.svx.fixspelltimer.patch
- drop integrated openoffice.org-3.3.0.ooo108246.svx.hide-sql-group-when-inactive.patch
- drop integrated openoffice.org-3.2.0.ooo95369.sw.sortedobjs.patch
- drop integrated openoffice.org-3.2.0.ooo110142.svx.safercolornames.patch
- drop integrated openoffice.org-3.3.0.ooo111758.sd.xerror.patch
- drop integrated openoffice.org-3.2.0.ooo111741.extras.malformed-xml-file.patch
- drop integrated openoffice.org-3.3.0.ooo112059.sw.avoid-null-ptr-deref.patch
- drop integrated openoffice.org-3.3.0.ooo100686.wizards.types.not.mediatypes.patch
- drop integrated workspace.vcl113.patch
- drop integrated openoffice.org-3.3.0.ooo112384.sw.export.doc.styledoesntexist.patch
- drop integrated workspace.cmcfixes77.patch
- drop integrated workspace.vcl114.patch
- drop integrated openoffice.org-3.3.0.ooo106591.sal.tradcopy.patch
- drop integrated workspace.vcl115.patch
- drop integrated workspace.cmcfixes78.patch
- drop integrated openoffice.org-3.3.0.ooo114012.sd.bada11ychain.patch
- drop integrated workspace.cmcfixes79.patch
- drop integrated openoffice.org-3.3.0.ooo114703.vcl.betterlocalize.font.patch
- drop integrated openoffice.org-3.3.0.rh638185.editeng.cjkctlhtmlsizes.patch
- drop integrated openoffice.org-3.3.0.rh637738.libgcrypt.addmutex.patch
- drop integrated openoffice.org-3.2.0.rh632236.writerfilter.cleanup-cell-props.patch
- drop workspace.gtk3.patch

* Wed Oct 06 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.1-2
- Related: rhbz#639945 pull in review changes
  + redland build-fix
  + replace awk script
  + validate .destop files

* Wed Sep 29 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.1-1
- initial import of the leviathan
