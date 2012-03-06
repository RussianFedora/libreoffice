%define libo_version 3.5.1
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
#%define source_url http://download.documentfoundation.org/libreoffice/src/%{libo_version}
%define source_url http://dev-builds.libreoffice.org/pre-releases/src

%if %{langpacks}
%if %{defined rhel} && 0%{?rhel} < 7
%define langpack_langs en-US af ar bg bn ca cs cy da de dz el es et eu fi fr ga gl gu he hi hr hu it ja ko kn lt mai ml nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-CN zh-TW zu
%else
%define langpack_langs en-US af ar as bg bn ca cs cy da de dz el es et eu fa fi fr ga gl gu he hi hr hu it ja ko kn lt lv mai ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-CN zh-TW zu
%endif
%define with_lang --with-lang="%{langpack_langs}"
%else
%define langpack_langs en-US
%define with_lang ''
%endif

%bcond_without binfilter

Summary:        Free Software Productivity Suite
Name:           libreoffice
Epoch:          1
Version:        %{libo_version}.2
Release:        1%{?dist}
License:        (MPLv1.1 or LGPLv3+) and LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and Public Domain and ASL 2.0 and Artistic
Group:          Applications/Productivity
URL:            http://www.documentfoundation.org/develop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        http://dev-builds.libreoffice.org/pre-releases/src/libreoffice-core-%{version}.tar.xz
Source1:        http://dev-builds.libreoffice.org/pre-releases/src/libreoffice-binfilter-%{version}.tar.xz
Source2:        http://dev-builds.libreoffice.org/pre-releases/src/libreoffice-help-%{version}.tar.xz
Source3:        http://dev-builds.libreoffice.org/pre-releases/src/libreoffice-translations-%{version}.tar.xz
Source4:        http://dev-www.libreoffice.org/extern/185d60944ea767075d27247c3162b3bc-unowinreg.dll
Source5:        redhat-langpacks.tar.gz
Source6:        libreoffice-multiliblauncher.sh
Source7:        http://hg.services.openoffice.org/binaries/fdb27bfe2dbe2e7b57ae194d9bf36bab-SampleICC-1.3.2.tar.gz
Source8:        http://hg.services.openoffice.org/binaries/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source9:        http://hg.services.openoffice.org/binaries/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
Source10:       http://hg.services.openoffice.org/binaries/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source11:       http://hg.services.openoffice.org/binaries/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
Source12:       http://hg.services.openoffice.org/binaries/ada24d37d8d638b3d8a9985e80bc2978-source-9.0.0.7-bj.zip
Source13:       http://hg.services.openoffice.org/binaries/18f577b374d60b3c760a3a3350407632-STLport-4.5.tar.gz
#Unfortunately later versions of hsqldb changed the file format, so if we use a later version we loose
#backwards compatability.
Source14:       http://hg.services.openoffice.org/binaries/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
%if %{defined rhel} && 0%{?rhel} < 7
Source15:       http://dev-www.libreoffice.org/src/0ff7d225d087793c8c2c680d77aac3e7-mdds_0.5.3.tar.bz2
Source16:       http://hg.services.openoffice.org/binaries/067201ea8b126597670b5eff72e1f66c-mythes-1.2.0.tar.gz
Source17:       http://dev-www.libreoffice.org/src/0981bda6548a8c8233ffce2b6e4b2a23-mysql-connector-c++-1.1.0.tar.gz
Source18:       http://dev-www.libreoffice.org/src/d28864eb2b59bb57b034c0d4662a3cee-libvisio-0.0.15.tar.bz2
Source19:       http://dev-www.libreoffice.org/src/e1c178b18f130b40494561f02bc1a948-libexttextcat-3.2.0.tar.bz2
Source20:       http://dev-www.libreoffice.org/src/7c2549f6b0a8bb604e6c4c729ffdcfe6-libcmis-0.1.0.tar.gz
Source21:       http://dev-www.libreoffice.org/src/48d8169acc35f97e05d8dcdfd45be7f2-lucene-2.3.2.tar.gz
Source22:	http://dev-www.libreoffice.org/src/48d647fbd8ef8889e5a7f422c1bfda94-clucene-core-2.3.3.4.tar.gz
Source23:	http://dev-www.libreoffice.org/src/061a9f17323117c9358ed60f33ecff78-postgresql-9.1.1.tar.bz2
Source24:       http://dev-www.libreoffice.org/src/3bf481ca95109b14435125c0dd1f2217-graphite2-1.0.3.tgz
Source25:       http://dev-www.libreoffice.org/src/9d283e02441d8cebdcd1e5d9df227d67-libwpg-0.2.1.tar.bz2
Source26:       http://dev-www.libreoffice.org/src/c01351d7db2b205de755d58769288224-libwpd-0.9.4.tar.bz2
Source27:       http://dev-www.libreoffice.org/src/34dd7951abbda99b7a75a09993a37965-libwps-0.2.4.tar.bz2
Source28:       http://dev-www.libreoffice.org/src/ca66e26082cab8bb817185a116db809b-redland-1.0.8.tar.gz
Source29:       http://dev-www.libreoffice.org/src/284e768eeda0e2898b0d5bf7e26a016e-raptor-1.4.18.tar.gz
Source30:       http://dev-www.libreoffice.org/src/fca8706f2c4619e2fa3f8f42f8fc1e9d-rasqal-0.9.16.tar.gz
%endif

BuildRequires:  zip, findutils, autoconf, flex, bison, icu, gperf, gcc-c++
BuildRequires:  binutils, java-devel, boost-devel
BuildRequires:  python-devel, expat-devel, libxml2-devel, libxslt-devel, bc
BuildRequires:  neon-devel, libcurl-devel, libidn-devel, pam-devel, cups-devel
BuildRequires:  libXext-devel, libXt-devel, libICE-devel, libjpeg-devel, make
BuildRequires:  gecko-devel, libwpd-devel, hunspell-devel, unixODBC-devel
BuildRequires:  sane-backends-devel, libicu-devel, libXinerama-devel
BuildRequires:  freetype-devel, gtk2-devel, desktop-file-utils, hyphen-devel
BuildRequires:  evolution-data-server-devel, nss-devel, zlib-devel
BuildRequires:  gstreamer-devel, gstreamer-plugins-base-devel, openssl-devel
BuildRequires:  lpsolve-devel, bsh, lucene, lucene-contrib, perl(Archive::Zip)
BuildRequires:  mesa-libGLU-devel, redland-devel, ant, ant-apache-regexp, rsync
BuildRequires:  jakarta-commons-codec, jakarta-commons-httpclient, cppunit-devel
BuildRequires:  jakarta-commons-lang, poppler-devel, fontpackages-devel
BuildRequires:  pentaho-reporting-flow-engine, vigra-devel, librsvg2-devel
BuildRequires:  GConf2-devel, ORBit2-devel, postgresql-devel
BuildRequires:  font(:lang=en)
%if %{defined rhel} && 0%{?rhel} < 7
BuildRequires:  hsqldb libdb-devel
%else
BuildRequires:  mdds-devel, mythes-devel, graphite2-devel, libwpg-devel
BuildRequires:  libwps-devel, junit, perl(Digest::MD5), libdb-devel
BuildRequires:  mysql-connector-c++-devel, poppler-cpp-devel
BuildRequires:  libcmis-devel, libexttextcat-devel, libvisio-devel
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
Patch7:  libreoffice-installfix.patch
%if %{defined rhel} && 0%{?rhel} < 7
Patch8: libreoffice-libwpd08-1.patch
Patch9: libreoffice-libwpd08-2.patch
Patch10: 0001-wpsimport-writerperfect.diff-WPS-Import-filter-core-.patch
Patch11: libreoffice-gcj.patch
Patch12: libreoffice-rhel6poppler.patch
Patch13: libreoffice-rhel6langs.patch
%endif
%if %{with binfilter}
Patch14: 0001-move-binfilter-mime-types-into-extra-.desktop-file.patch
%endif
Patch15: 0001-Resolves-rhbz-788042-skip-splashscreen-with-quicksta.patch
Patch16: 0001-make-hsqldb-build-with-java-1.7.patch
Patch17: libreoffice-ensure-non-broken-xml-tree.patch
Patch18: 0001-preserve-timestamps-for-.py-files.patch
Patch19: 0001-Resolves-rhbz-788045-swriter-help-etc-doesn-t-show-h.patch

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define instdir %{_libdir}
%define baseinstdir %{instdir}/libreoffice
%define ureinstdir %{baseinstdir}/ure
%define sdkinstdir %{baseinstdir}/sdk
%define fontname opensymbol

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
Obsoletes: openoffice.org-testtools < 1:3.3.1
Obsoletes: libreoffice-testtools < 1:3.4.99.1
%if %{defined rhel} && 0%{?rhel} < 7
Provides: openoffice.org-testtools = 1:3.3.0
Obsoletes: openoffice.org2-testtools < 1:3.0.0
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
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
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
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
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

%package nlpsolver
Summary: Non-linear solver engine for LibreOffice Calc
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core

%description nlpsolver
A non-linear solver engine for Calc as an alternative to the default linear
programming model when more complex, nonlinear programming is required.

%package ogltrans
Summary: 3D OpenGL slide transitions for LibreOffice
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
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
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
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
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
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
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
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
Requires: %{name}-ogltrans = %{epoch}:%{version}-%{release}
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

%package postgresql
Summary: PostgreSQL connector for LibreOffice
Group: Applications/Productivity
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: postgresql-libs

%description postgresql
A PostgreSQL connector for the database front-end for LibreOffice. Allows
creation and management of PostgreSQL databases through a GUI.

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

%if %{with binfilter}
%package binfilter
Summary: Legacy binary filters for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}

%description binfilter
Filters for old StarOffice binary formats.
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
# TODO does it make sense to install this?
%{baseinstdir}/program/gdbtrace
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
Provides: %{obs}-%{-o*} = 1:3.3.1.1  \
}%{!-o: \
%{-O: \
Obsoletes: openoffice.org-i18n < 1.9.0 \
Obsoletes: %{obs}-%{lang} < %{obsv} \
Provides: %{obs}-%{lang} = 1:3.3.1.1  \
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
%doc solver/unxlng*/bin/ure/LICENSE \
%dir %{_datadir}/autocorr \
%{!-X:%{_datadir}/autocorr/acor_%{lang}-*} \
%*


%if %{langpacks}

%langpack -l af -n Afrikaans -F -H -Y -A -o af_ZA -V -x af_ZA -S
%langpack -l ar -n Arabic -F -H -O -X -S
#langpack -l as -n Assamese -F -H -Y -o as_IN -x as_IN -S
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
%if %{undefined rhel} || 0%{?rhel} >= 7
%langpack -l fa -n Farsi -A -H -Y -S
%endif
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
%langpack -l hi -n Hindi -F -H -Y -o hi_IN -v hi-IN -x hi_IN -S
%langpack -l hr -n Croatian -F -H -Y -A -o hr_HR -V -x hr_HR -S
%langpack -l hu -n Hungarian -F -H -Y -M -A -o hu_HU -V -x hu_HU -S
%langpack -l it -n Italian -F -H -Y -M -A -O -X -S
%langpack -l ja -n Japanese -F -A -o ja_JP -V -x ja_JP -S
%langpack -l kn -n Kannada -F -H -Y -o kn_IN -x ka_IN -S
%langpack -l ko -n Korean -F -H -A -o ko_KR -V -x ko_KR -S
%{baseinstdir}/share/registry/korea.xcd

%langpack -l lt -n Lithuanian -F -H -Y -A -o lt_LT -V -x lt_LT -S
%if %{undefined rhel} || 0%{?rhel} >= 7
%langpack -l lv -n Latvian -F -H -Y -M -S
%endif
%langpack -l mai -n Maithili -F -o mai_IN -S
%langpack -l ml -n Malayalam -F -H -Y -o ml_IN -x ml_IN -S
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
%langpack -l pt-BR -n %{langpack_lang} -f pt -h pt -y pt -m pt -a pt -o pt_BR -p pt_BR -V -x pt_BR -S
%langpack -l pt-PT -n Portuguese -f pt -h pt -y pt -m pt -a pt -o pt_PT -p pt_PT -v pt -X -s pt
%langpack -l ro -n Romanian -F -H -Y -M -O -S
%langpack -l ru -n Russian -F -H -Y -M -A -O -X -S
%if %{undefined rhel} || 0%{?rhel} >= 7
%langpack -l si -n Sinhalese -F -H -O -S
%endif
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
%{baseinstdir}/share/registry/ctlseqcheck_th.xcd

%langpack -l tn -n Tswana -F -H -o tn_ZA -V -x tn_ZA -S
%langpack -l tr -n Turkish -F -A -o tr_TR -V -X -S
%langpack -l ts -n Tsonga -F -H -o ts_ZA -V -x ts_ZA -S
%langpack -l uk -n Ukrainian -F -H -Y -M -O -S
%langpack -l ve -n Venda -F -H -o ve_ZA -S
%langpack -l xh -n Xhosa -F -H -o xh_ZA -S
%define langpack_lang Simplified Chinese
%langpack -l zh-Hans -n %{langpack_lang} -f zh-cn -a zh -o zh_CN -p zh_CN -v zh-CN -x zh_CN -s zh-CN
%define langpack_lang Traditional Chinese
%langpack -l zh-Hant -n %{langpack_lang} -f zh-tw -a zh -o zh_TW -p zh_TW -v zh-TW -x zh_TW -s zh-TW
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
%setup -q -c -a 1 -a 2 -a 3
rm -rf git-hooks */git-hooks
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
%patch5  -p1 -b .ooo101274.opening-a-directory.patch
%patch6  -p1 -b .ooo105784.vcl.sniffscriptforsubs.patch
%patch7  -p1 -b .libreoffice-installfix.patch
%if %{defined rhel} && 0%{?rhel} < 7
#%patch8 -p1 -b .libwpd08-1.patch
#%patch9 -p1 -R -b .libreoffice-libwpd08-2.patch
#%patch10 -p1 -R -b .wpsimport
#%patch11 -p1 -b .gcj.patch
%patch12 -p0 -b .rhel6poppler.patch
#%patch13 -p0 -b .rhel6langs.patch
%endif
%if %{with binfilter}
%patch14 -p1 -b .move-binfilter-mime-types-into-extra-.desktop-file.patch
%endif
%patch15 -p1 -b .rhbz788042-skip-splashscreen-with-quicksta.patch
%patch16 -p1 -b .make-hsqldb-build-with-java-1.7.patch
%patch17 -p1 -b .ensure-non-broken-xml-tree.patch
%patch18 -p1 -b .preserve-timestamps-for-.py-files.patch
%patch19 -p1 -b .rhbz788045-swriter-help-etc-doesn-t-show-h.patch

# TODO: check this
# these are horribly incomplete--empty translations and copied english
# strings with spattering of translated strings
rm -rf translations/source/{gu,he,hr}/helpcontent2

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

#%if %{defined rhel}
#%if 0%{?rhel} < 7
#%define distrooptions --disable-graphite --without-system-mythes \
#    --without-system-mdds --without-junit --without-system-mysql-cppconn
#%else
#%define distrooptions --without-system-hsqldb
#%endif
#%else
#%define distrooptions --without-system-hsqldb --enable-kde4
#%endif

autoconf
%configure \
 %vendoroption --with-num-cpus=$NBUILDS --with-max-jobs=$NDMAKES \
 --with-build-version="Ver: %{version}-%{release}" --with-unix-wrapper=%{name} \
 --disable-ldap --disable-epm --disable-mathmldtd \
 --disable-gnome-vfs --enable-gio --enable-symbols --enable-lockdown \
 --enable-evolution2 --enable-dbus --enable-opengl --enable-vba \
 --enable-ext-presenter-minimizer --enable-ext-nlpsolver \
 --enable-ext-presenter-console --enable-ext-pdfimport \
 --enable-ext-wiki-publisher --enable-ext-report-builder \
 --enable-ext-scripting-beanshell --enable-ext-scripting-javascript \
 --without-system-servlet-api \
 --with-system-jars --with-vba-package-format="builtin" \
 --with-system-libs --with-system-headers --with-system-mozilla \
 --without-system-mozilla-headers --with-system-mythes --with-system-dicts \
 --without-system-saxon --with-external-dict-dir=/usr/share/myspell \
 --without-system-lucene --without-system-postgresql \
 --without-system-mdds --without-system-libexttextcat \
 --without-system-libwpd --without-system-libwps --without-system-libwpg \
 --without-system-graphite --without-junit --without-system-libvisio \
 --without-system-libcmis --without-system-redland \
 --without-myspell-dicts --without-fonts --without-ppds --without-afms \
 %{with_lang} --with-poor-help-localizations="$POORHELPS" \
 --with-external-tar=`pwd`/ext_sources --with-java-target-version=1.5 \
 --without-system-sampleicc \
 --without-system-mythes --without-system-mysql-cppconn \
 %{?with_binfilter:--enable-binfilter}

mkdir -p ext_sources
cp %{SOURCE4} ext_sources
cp %{SOURCE7} ext_sources
cp %{SOURCE8} ext_sources
cp %{SOURCE9} ext_sources
cp %{SOURCE10} ext_sources
cp %{SOURCE11} ext_sources
cp %{SOURCE12} ext_sources
cp %{SOURCE13} ext_sources
cp %{SOURCE14} ext_sources
%if %{defined rhel} && 0%{?rhel} < 7
cp %{SOURCE15} ext_sources
cp %{SOURCE16} ext_sources
cp %{SOURCE17} ext_sources
cp %{SOURCE18} ext_sources
cp %{SOURCE19} ext_sources
cp %{SOURCE20} ext_sources
cp %{SOURCE21} ext_sources
cp %{SOURCE22} ext_sources
cp %{SOURCE23} ext_sources
cp %{SOURCE24} ext_sources
cp %{SOURCE25} ext_sources
cp %{SOURCE26} ext_sources
cp %{SOURCE27} ext_sources
cp %{SOURCE28} ext_sources
cp %{SOURCE29} ext_sources
cp %{SOURCE30} ext_sources
%endif
touch src.downloaded

. ./Env.Host.sh
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


%install
rm -rf $RPM_BUILD_ROOT
source ./Env.Host.sh
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
mv ../unxlng*.pro/LibreOffice_SDK/installed/install/en-US/sdk $RPM_BUILD_ROOT/%{sdkinstdir}
cd ../../

#configure sdk
pushd $RPM_BUILD_ROOT/%{sdkinstdir}
    for file in setsdkenv_unix.csh setsdkenv_unix.sh ; do
        sed -e "s,@OO_SDK_NAME@,sdk," \
            -e "s,@OO_SDK_HOME@,%{sdkinstdir}," \
            -e "s,@OFFICE_HOME@,%{baseinstdir}," \
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

#ensure a template dir for each lang
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/template
for I in %{langpack_langs}; do
    mkdir -p $I
done
popd

#Set some aliases to canonical autocorrect language files for locales with matching languages
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/autocorr

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
nl_NL_aliases="nl-AW"
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
mv -f $RPM_BUILD_ROOT/%{baseinstdir}/share/autocorr $RPM_BUILD_ROOT/%{_datadir}/autocorr
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
ms      nohelp  western         nb      help    western \
nl      help    western        	nn      help    western \
nr      nohelp  western         nso     nohelp  western \
or      nohelp  ctl            	pa-IN   nohelp  ctl     \
pl      help    western         pt      help    western \
pt-BR   help    western         ro      nohelp  western \
ru      help    western        	sh      nohelp  western \
si      help    ctl             sk      help    western \
sl      help    western         sr      nohelp  western \
ss      nohelp  western         st      nohelp  western \
sv      help    western         ta      nohelp  ctl     \
te      nohelp  western         th      nohelp  ctlseqcheck \
tn      nohelp  western         tr      help    western \
ts      nohelp  western         uk      help    western \
ur      nohelp  western         ve      nohelp  western \
xh      nohelp  western         zh-CN   help    cjk     \
zh-TW   help    cjk             zu      nohelp  western \
)

tar xzf %{SOURCE5}

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
     rm -f $RPM_BUILD_ROOT/%{baseinstdir}/share/registry/ctl_$lang.xcd
   fi
   i=$[i+1]
done

#rhbz#452379 clump serbian translations together
cat sh.filelist >> sr.filelist

%endif

#remove it in case we didn't build with gcj
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/classes/sandbox.jar

#remove dummy .dat files
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/root?.dat

#remove if we do not build with kde support
%if %{defined rhel}
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/kde-open-url
%endif

#set standard permissions for rpmlint
find $RPM_BUILD_ROOT/%{baseinstdir} -exec chmod +w {} \;
find $RPM_BUILD_ROOT/%{baseinstdir} -type d -exec chmod 0755 {} \;

# move python bits into site-packages
mkdir -p $RPM_BUILD_ROOT/%{python_sitearch}
pushd $RPM_BUILD_ROOT/%{python_sitearch}
echo "import sys, os" > uno.py
echo "sys.path.append('%{baseinstdir}/program')" >> uno.py
echo "os.putenv('URE_BOOTSTRAP', 'vnd.sun.star.pathname:%{baseinstdir}/program/fundamentalrc')" >> uno.py
cat $RPM_BUILD_ROOT/%{baseinstdir}/program/uno.py >> uno.py
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/uno.py*
mv -f $RPM_BUILD_ROOT/%{baseinstdir}/program/unohelper.py* .
popd

# rhbz#477435 package opensymbol separately
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/fonts/truetype
install -d -m 0755 %{buildroot}%{_fontdir}
install -p -m 0644 *.ttf %{buildroot}%{_fontdir}
popd
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/share/fonts

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

cp -f %{SOURCE6} $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/LAUNCHER/unopkg/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/BRAND/libreoffice/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/unopkg

cp -f %{SOURCE6} $RPM_BUILD_ROOT/%{_bindir}/libreoffice
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
echo "NoDisplay=true" >> startcenter.desktop
# rhbz#491159 temporarily remove NoDisplay=true from qstart.desktop
sed -i -e "/NoDisplay=true/d" qstart.desktop
# relocate the .desktop and icon files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
for app in base %{?with_binfilter:binfilter} calc draw impress javafilter math startcenter writer; do
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
    cp -p $icon $RPM_BUILD_ROOT/%{_datadir}/`echo $icon | sed -e s@office$ICONVERSION@office@ | sed -e s@office$PRODUCTVERSION@office@`
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

mkdir -p $RPM_BUILD_ROOT/%{baseinstdir}/share/psprint/driver
cp -p psprint_config/configuration/ppds/SGENPRT.PS $RPM_BUILD_ROOT/%{baseinstdir}/share/psprint/driver/SGENPRT.PS

# rhbz#452385 to auto have postgres in classpath if subsequently installed
# rhbz#465664 to get lucene working for functional help
sed -i -e "s#URE_MORE_JAVA_CLASSPATH_URLS.*#& file:///usr/share/java/lucene.jar file:///usr/share/java/lucene-contrib/lucene-analyzers.jar file:///usr/share/java/postgresql-jdbc.jar#" $RPM_BUILD_ROOT/%{baseinstdir}/program/fundamentalrc

export DESTDIR=$RPM_BUILD_ROOT
install-gdb-printers -a %{_datadir}/gdb/auto-load%{baseinstdir} -c -i %{baseinstdir} -p %{_datadir}/libreoffice/gdb


%check
source ./Env.Host.sh
cd smoketestoo_native
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
%dir %{baseinstdir}
%dir %{baseinstdir}/help
%docdir %{baseinstdir}/help/en
%dir %{baseinstdir}/help/en
%{baseinstdir}/help/en/default.css
%{baseinstdir}/help/en/err.html
%{baseinstdir}/help/en/highcontrast1.css
%{baseinstdir}/help/en/highcontrast2.css
%{baseinstdir}/help/en/highcontrastblack.css
%{baseinstdir}/help/en/highcontrastwhite.css
%{baseinstdir}/help/en/sbasic.*
%{baseinstdir}/help/en/schart.*
%{baseinstdir}/help/en/shared.*
%{baseinstdir}/help/idxcaption.xsl
%{baseinstdir}/help/idxcontent.xsl
%{baseinstdir}/help/main_transform.xsl
%{baseinstdir}/presets
%dir %{baseinstdir}/program
%{baseinstdir}/program/addin
%{baseinstdir}/program/basprov.uno.so
%{baseinstdir}/program/canvasfactory.uno.so
%{baseinstdir}/program/cde-open-url
%dir %{baseinstdir}/program/classes
%{baseinstdir}/program/classes/agenda.jar
%{baseinstdir}/program/classes/commonwizards.jar
%{baseinstdir}/program/classes/fax.jar
%{baseinstdir}/program/classes/form.jar
%{baseinstdir}/program/classes/query.jar
%{baseinstdir}/program/classes/letter.jar
%{baseinstdir}/program/classes/LuceneHelpWrapper.jar
%{baseinstdir}/program/classes/officebean.jar
%{baseinstdir}/program/classes/report.jar
%{baseinstdir}/program/classes/saxon9.jar
%{baseinstdir}/program/classes/ScriptFramework.jar
%{baseinstdir}/program/classes/ScriptProviderForJava.jar
%{baseinstdir}/program/classes/table.jar
%{baseinstdir}/program/classes/unoil.jar
%{baseinstdir}/program/classes/web.jar
%{baseinstdir}/program/classes/XMergeBridge.jar
%{baseinstdir}/program/classes/xmerge.jar
%{baseinstdir}/program/classes/XSLTFilter.jar
%{baseinstdir}/program/classes/XSLTValidate.jar
%{baseinstdir}/program/cmdmail.uno.so
%{baseinstdir}/program/libdeployment.so
%{baseinstdir}/program/libdeploymentgui.so
%{baseinstdir}/program/dlgprov.uno.so
%{baseinstdir}/program/expwrap.uno.so
%{baseinstdir}/program/fastsax.uno.so
%{baseinstdir}/program/fpicker.uno.so
%{baseinstdir}/program/fps_office.uno.so
%{baseinstdir}/program/gengal
%{baseinstdir}/program/gengal.bin
%{baseinstdir}/program/gnome-open-url
%{baseinstdir}/program/gnome-open-url.bin
%{baseinstdir}/program/hatchwindowfactory.uno.so
%{baseinstdir}/program/i18nsearch.uno.so
%{baseinstdir}/program/libacclo.so
%{baseinstdir}/program/libavmedia*.so
%{baseinstdir}/program/libbasctllo.so
%{baseinstdir}/program/libbiblo.so
%{baseinstdir}/program/libcached1.so
%{baseinstdir}/program/libcanvastoolslo.so
%{baseinstdir}/program/libchart*lo.so
%{baseinstdir}/program/libcollator_data.so
%{baseinstdir}/program/libcppcanvaslo.so
%{baseinstdir}/program/libctllo.so
%{baseinstdir}/program/libcuilo.so
%{baseinstdir}/program/libdbalo.so
%{baseinstdir}/program/libdbaselo.so
%{baseinstdir}/program/libdbaxmllo.so
%{baseinstdir}/program/libdbmmlo.so
%{baseinstdir}/program/libdbpool2.so
%{baseinstdir}/program/libdbtoolslo.so
%{baseinstdir}/program/libdbulo.so
%{baseinstdir}/program/libdeploymentmisclo.so
%{baseinstdir}/program/libdesktop_detectorlo.so
%{baseinstdir}/program/libdict_ja.so
%{baseinstdir}/program/libdict_zh.so
%{baseinstdir}/program/libdrawinglayerlo.so
%{baseinstdir}/program/libeditenglo.so
%{baseinstdir}/program/libembobj.so
%{baseinstdir}/program/libemboleobj.so
%{baseinstdir}/program/libevoab*.so
%{baseinstdir}/program/libevtattlo.so
%{baseinstdir}/program/libegilo.so
%{baseinstdir}/program/libemelo.so
%{baseinstdir}/program/libepblo.so
%{baseinstdir}/program/libepglo.so
%{baseinstdir}/program/libepplo.so
%{baseinstdir}/program/libepslo.so
%{baseinstdir}/program/libeptlo.so
%{baseinstdir}/program/liberalo.so
%{baseinstdir}/program/libetilo.so
%{baseinstdir}/program/libexplo.so
%{baseinstdir}/program/libicdlo.so
%{baseinstdir}/program/libicglo.so
%{baseinstdir}/program/libidxlo.so
%{baseinstdir}/program/libimelo.so
%{baseinstdir}/program/libindex_data.so
%{baseinstdir}/program/libipblo.so
%{baseinstdir}/program/libipdlo.so
%{baseinstdir}/program/libipslo.so
%{baseinstdir}/program/libiptlo.so
%{baseinstdir}/program/libipxlo.so
%{baseinstdir}/program/libiralo.so
%{baseinstdir}/program/libitglo.so
%{baseinstdir}/program/libitilo.so
%{baseinstdir}/program/libofficebeanlo.so
%{baseinstdir}/program/liboooimprovecorelo.so
%{baseinstdir}/program/libfilelo.so
%{baseinstdir}/program/libfilterconfiglo.so
%{baseinstdir}/program/libflatlo.so
%{baseinstdir}/program/libfrmlo.so
%{baseinstdir}/program/libguesslanglo.so
%{baseinstdir}/program/libhelplinkerlo.so
%{baseinstdir}/program/libhyphenlo.so
%{baseinstdir}/program/libi18nregexplo.so
%{baseinstdir}/program/libjdbclo.so
%{baseinstdir}/program/liblnglo.so
%{baseinstdir}/program/libloglo.so
%{baseinstdir}/program/liblocaledata_en.so
%{baseinstdir}/program/liblocaledata_es.so
%{baseinstdir}/program/liblocaledata_euro.so
%{baseinstdir}/program/liblocaledata_others.so
%{baseinstdir}/program/libmcnttype.so
%{baseinstdir}/program/libmozbootstrap.so
%{baseinstdir}/program/libmsfilterlo.so
%{baseinstdir}/program/mtfrenderer.uno.so
%{baseinstdir}/program/libmysqllo.so
%{baseinstdir}/program/libodbclo.so
%{baseinstdir}/program/libodbcbaselo.so
%{baseinstdir}/program/liboffacclo.so
%{baseinstdir}/program/libooxlo.so
%{baseinstdir}/program/libpcrlo.so
%{baseinstdir}/program/libpdffilterlo.so
%{baseinstdir}/program/libpllo.so
%{baseinstdir}/program/libprotocolhandlerlo.so
%{baseinstdir}/program/libqstart_gtklo.so
%{baseinstdir}/program/librecentfile.so
%{baseinstdir}/program/libreslo.so
%{baseinstdir}/program/libsaxlo.so
%{baseinstdir}/program/libscnlo.so
%{baseinstdir}/program/libscriptframe.so
%{baseinstdir}/program/libsdlo.so
%{baseinstdir}/program/libsdfiltlo.so
%{baseinstdir}/program/libsdbc2.so
%{baseinstdir}/program/libsdbtlo.so
%{baseinstdir}/program/libsddlo.so
%{baseinstdir}/program/libsduilo.so
%{baseinstdir}/program/libspalo.so
%{baseinstdir}/program/libspelllo.so
%{baseinstdir}/program/libsrtrs1.so
%{baseinstdir}/program/libsvxlo.so
%{baseinstdir}/program/libsvxcorelo.so
%{baseinstdir}/program/libswlo.so
%{baseinstdir}/program/libtextconv_dict.so
%{baseinstdir}/program/libtextconversiondlgslo.so
%{baseinstdir}/program/libtvhlp1.so
%{baseinstdir}/program/libodfflatxmllo.so
%{baseinstdir}/program/libucbhelper4gcc3.so
%{baseinstdir}/program/libucpchelp1.so
%{baseinstdir}/program/libucpdav1.so
%{baseinstdir}/program/libucpftp1.so
%{baseinstdir}/program/libucphier1.so
%{baseinstdir}/program/libucppkg1.so
%{baseinstdir}/program/libunordflo.so
%{baseinstdir}/program/libunopkgapp.so
%{baseinstdir}/program/libunoxmllo.so
%{baseinstdir}/program/libupdchklo.so
%{baseinstdir}/program/libuuilo.so
%{baseinstdir}/program/libvbahelperlo.so
%{baseinstdir}/program/libvclplug_genlo.so
%{baseinstdir}/program/libvclplug_gtklo.so
%if %{undefined rhel} || 0%{?rhel} >= 7
%{baseinstdir}/program/libwpgimportlo.so
%endif
%{baseinstdir}/program/libxmlfalo.so
%{baseinstdir}/program/libxmlfdlo.so
%{baseinstdir}/program/libxmxlo.so
%{baseinstdir}/program/libxoflo.so
%{baseinstdir}/program/libxsec_fw.so
%{baseinstdir}/program/libxsec_xmlsec.so
%{baseinstdir}/program/libxsltdlglo.so
%{baseinstdir}/program/libxsltfilterlo.so
%{baseinstdir}/program/libxstor.so
%{baseinstdir}/program/migrationoo2.uno.so
%{baseinstdir}/program/migrationoo3.uno.so
%{baseinstdir}/program/msforms.uno.so
%{baseinstdir}/program/nsplugin
%{baseinstdir}/program/open-url
%{baseinstdir}/program/types/offapi.rdb
%{baseinstdir}/program/passwordcontainer.uno.so
%{baseinstdir}/program/pagein-common
%{baseinstdir}/program/plugin
%{baseinstdir}/program/pluginapp.bin
%dir %{baseinstdir}/program/resource
%{baseinstdir}/program/resource/avmediaen-US.res
%{baseinstdir}/program/resource/accen-US.res
%{baseinstdir}/program/resource/basctlen-US.res
%{baseinstdir}/program/resource/biben-US.res
%{baseinstdir}/program/resource/calen-US.res
%{baseinstdir}/program/resource/chartcontrolleren-US.res
%{baseinstdir}/program/resource/cuien-US.res
%{baseinstdir}/program/resource/dbaen-US.res
%{baseinstdir}/program/resource/dbmmen-US.res
%{baseinstdir}/program/resource/dbuen-US.res
%{baseinstdir}/program/resource/dbwen-US.res
%{baseinstdir}/program/resource/deploymenten-US.res
%{baseinstdir}/program/resource/deploymentguien-US.res
%{baseinstdir}/program/resource/dkten-US.res
%{baseinstdir}/program/resource/editengen-US.res
%{baseinstdir}/program/resource/epsen-US.res
%{baseinstdir}/program/resource/euren-US.res
%{baseinstdir}/program/resource/fps_officeen-US.res
%{baseinstdir}/program/resource/frmen-US.res
%{baseinstdir}/program/resource/fween-US.res
%{baseinstdir}/program/resource/galen-US.res
%{baseinstdir}/program/resource/impen-US.res
%{baseinstdir}/program/resource/ofaen-US.res
%{baseinstdir}/program/resource/pcren-US.res
%{baseinstdir}/program/resource/pdffilteren-US.res
%{baseinstdir}/program/resource/sanen-US.res
%{baseinstdir}/program/resource/sben-US.res
%{baseinstdir}/program/resource/sden-US.res
%{baseinstdir}/program/resource/sfxen-US.res
%{baseinstdir}/program/resource/spaen-US.res
%{baseinstdir}/program/resource/sdbten-US.res
%{baseinstdir}/program/resource/svlen-US.res
%{baseinstdir}/program/resource/svten-US.res
%{baseinstdir}/program/resource/svxen-US.res
%{baseinstdir}/program/resource/swen-US.res
%{baseinstdir}/program/resource/textconversiondlgsen-US.res
%{baseinstdir}/program/resource/tken-US.res
%{baseinstdir}/program/resource/tplen-US.res
%{baseinstdir}/program/resource/uuien-US.res
%{baseinstdir}/program/resource/updchken-US.res
%{baseinstdir}/program/resource/upden-US.res
%{baseinstdir}/program/resource/vclen-US.res
%{baseinstdir}/program/resource/wzien-US.res
%{baseinstdir}/program/resource/xmlsecen-US.res
%{baseinstdir}/program/resource/xsltdlgen-US.res
%{baseinstdir}/program/senddoc
%{baseinstdir}/program/services/services.rdb
%{baseinstdir}/program/simplecanvas.uno.so
%{baseinstdir}/program/slideshow.uno.so
%{baseinstdir}/program/libsofficeapp.so
%{baseinstdir}/program/spadmin.bin
%{baseinstdir}/program/stringresource.uno.so
%{baseinstdir}/program/syssh.uno.so
%{baseinstdir}/program/ucpcmis1.uno.so
%{baseinstdir}/program/ucpexpand1.uno.so
%{baseinstdir}/program/ucpext.uno.so
%{baseinstdir}/program/ucptdoc1.uno.so
%{baseinstdir}/program/unorc
%{baseinstdir}/program/updatefeed.uno.so
%{baseinstdir}/ure-link
%{baseinstdir}/program/uri-encode
%{baseinstdir}/program/vbaevents.uno.so
%{baseinstdir}/program/vclcanvas.uno.so
%{baseinstdir}/program/versionrc
%{baseinstdir}/program/cairocanvas.uno.so
%dir %{baseinstdir}/share
%dir %{baseinstdir}/share/Scripts
%{baseinstdir}/share/Scripts/java
%{baseinstdir}/share/autotext
%{baseinstdir}/share/basic
%dir %{baseinstdir}/share/config
%{baseinstdir}/share/config/images.zip
%{baseinstdir}/share/config/images_crystal.zip
%{baseinstdir}/share/config/images_hicontrast.zip
%{baseinstdir}/share/config/images_oxygen.zip
%{baseinstdir}/share/config/images_tango.zip
%{baseinstdir}/share/config/javasettingsunopkginstall.xml
%{baseinstdir}/share/config/psetup.xpm
%{baseinstdir}/share/config/psetupl.xpm
%dir %{baseinstdir}/share/config/soffice.cfg
%{baseinstdir}/share/config/soffice.cfg/modules
%{baseinstdir}/share/config/symbol
%{baseinstdir}/share/config/webcast
%{baseinstdir}/share/config/wizard
%dir %{baseinstdir}/share/dtd
%{baseinstdir}/share/dtd/officedocument
%if %{defined rhel} && 0%{?rhel} < 7
%{baseinstdir}/share/fingerprint
%endif
%{baseinstdir}/share/gallery
%dir %{baseinstdir}/share/psprint
%config %{baseinstdir}/share/psprint/psprint.conf
%{baseinstdir}/share/psprint/driver
%dir %{baseinstdir}/share/registry
%{baseinstdir}/share/registry/gnome.xcd
%{baseinstdir}/share/registry/lingucomponent.xcd
%{baseinstdir}/share/registry/main.xcd
%{baseinstdir}/share/registry/oo-ad-ldap.xcd.sample
%{baseinstdir}/share/registry/oo-ldap.xcd.sample
%{baseinstdir}/share/registry/Langpack-en-US.xcd
%dir %{baseinstdir}/share/registry/res
%{baseinstdir}/share/registry/res/fcfg_langpack_en-US.xcd
%dir %{baseinstdir}/share/samples
%{baseinstdir}/share/samples/en-US
%dir %{baseinstdir}/share/template
%{baseinstdir}/share/template/en-US
%dir %{baseinstdir}/share/template/common
%{baseinstdir}/share/template/common/layout
%{baseinstdir}/share/template/wizard
%dir %{baseinstdir}/share/wordbook
%{baseinstdir}/share/wordbook/en-GB.dic
%{baseinstdir}/share/wordbook/en-US.dic
%{baseinstdir}/share/wordbook/sl.dic
%{baseinstdir}/share/wordbook/technical.dic
%dir %{baseinstdir}/share/xslt
%{baseinstdir}/share/xslt/common
%dir %{baseinstdir}/share/xslt/export
%{baseinstdir}/share/xslt/export/common
%{baseinstdir}/share/xslt/export/spreadsheetml
%{baseinstdir}/share/xslt/export/wordml
%dir %{baseinstdir}/share/xslt/import
%{baseinstdir}/share/xslt/import/common
%{baseinstdir}/share/xslt/import/spreadsheetml
%{baseinstdir}/share/xslt/import/wordml
%{baseinstdir}/program/liblnthlo.so
%{_bindir}/unopkg
#icons and mime
%{_datadir}/icons/*/*/*/libreoffice*
%{_datadir}/mime-info/libreoffice.*
%{baseinstdir}/program/libxmlsecurity.so
%{_datadir}/mime/packages/libreoffice.xml
%{baseinstdir}/program/configmgr.uno.so
%{baseinstdir}/program/desktopbe1.uno.so
%{baseinstdir}/program/fsstorage.uno.so
%{baseinstdir}/program/gconfbe1.uno.so
%{baseinstdir}/program/i18npool.uno.so
%{baseinstdir}/program/libbasegfxlo.so
%{baseinstdir}/program/libcomphelpgcc3.so
%{baseinstdir}/program/libfileacc.so
%{baseinstdir}/program/libfwelo.so
%{baseinstdir}/program/libfwilo.so
%{baseinstdir}/program/libfwklo.so
%{baseinstdir}/program/libfwllo.so
%{baseinstdir}/program/libfwmlo.so
%{baseinstdir}/program/libi18nisolang*.so
%{baseinstdir}/program/libi18npaper*.so
%{baseinstdir}/program/libi18nutilgcc3.so
%{baseinstdir}/program/libpackage2.so
%{baseinstdir}/program/libsblo.so
%{baseinstdir}/program/libsfxlo.so
%{baseinstdir}/program/libsotlo.so
%{baseinstdir}/program/libspllo.so
%{baseinstdir}/program/libspl_unxlo.so
%{baseinstdir}/program/libsvllo.so
%{baseinstdir}/program/libsvtlo.so
%{baseinstdir}/program/libtklo.so
%{baseinstdir}/program/libtllo.so
%{baseinstdir}/program/libucb1.so
%{baseinstdir}/program/libucpfile1.so
%{baseinstdir}/program/libutllo.so
%{baseinstdir}/program/libvcllo.so
%{baseinstdir}/program/libxcrlo.so
%{baseinstdir}/program/libxolo.so
%{baseinstdir}/program/localebe1.uno.so
%{baseinstdir}/program/ucpgio1.uno.so
%{baseinstdir}/program/types/oovbaapi.rdb
#share unopkg
%dir %{baseinstdir}/share/extensions
%{baseinstdir}/share/extensions/package.txt
%{baseinstdir}/program/unopkg
%{baseinstdir}/program/unopkg.bin
%{baseinstdir}/program/bootstraprc
%{baseinstdir}/program/fundamentalrc
%{baseinstdir}/program/setuprc
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
%{baseinstdir}/program/oosplash
%{baseinstdir}/program/shell/
%{baseinstdir}/share/config/images_brand.zip
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
%dir %{baseinstdir}
%{baseinstdir}/help/en/sdatabase.*
%dir %{baseinstdir}/program
%dir %{baseinstdir}/program/classes
%if %{undefined rhel} || 0%{?rhel} >= 7
%{baseinstdir}/program/classes/hsqldb.jar
%endif
%{baseinstdir}/program/classes/sdbc_hsqldb.jar
%{baseinstdir}/program/libabplo.so
%{baseinstdir}/program/libadabasuilo.so
%{baseinstdir}/program/libdbplo.so
%{baseinstdir}/program/libhsqldb.so
%{baseinstdir}/program/librpt*lo.so
%dir %{baseinstdir}/program/resource
%{baseinstdir}/program/resource/abpen-US.res
%{baseinstdir}/program/resource/adabasuien-US.res
%{baseinstdir}/program/resource/cnren-US.res
%{baseinstdir}/program/resource/dbpen-US.res
%{baseinstdir}/program/resource/rpten-US.res
%{baseinstdir}/program/resource/rptuien-US.res
%{baseinstdir}/program/resource/sdbclen-US.res
%{baseinstdir}/program/resource/sdberren-US.res
%{baseinstdir}/share/registry/base.xcd
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
%{baseinstdir}/program/classes/ScriptProviderForBeanShell.jar
%{baseinstdir}/program/services/scriptproviderforbeanshell.rdb
%{baseinstdir}/share/Scripts/beanshell

%files rhino
%defattr(-,root,root,-)
%{baseinstdir}/program/classes/js.jar
%{baseinstdir}/program/classes/ScriptProviderForJavaScript.jar
%{baseinstdir}/program/services/scriptproviderforjavascript.rdb
%{baseinstdir}/share/Scripts/javascript

%files wiki-publisher
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/wiki-publisher/license
%{baseinstdir}/share/extensions/wiki-publisher

%files nlpsolver
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/nlpsolver/help
%{baseinstdir}/share/extensions/nlpsolver

%files ogltrans
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/OGLTrans.uno.so
%dir %{baseinstdir}/share/config
%dir %{baseinstdir}/share/config/soffice.cfg
%dir %{baseinstdir}/share/config/soffice.cfg/simpress
%{baseinstdir}/share/config/soffice.cfg/simpress/transitions-ogl.xml
%{baseinstdir}/share/registry/ogltrans.xcd

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
%doc solver/unxlng*/bin/ure/LICENSE

%files calc
%defattr(-,root,root,-)
%dir %{baseinstdir}
%{baseinstdir}/help/en/scalc.*
%dir %{baseinstdir}/program
%{baseinstdir}/program/libanalysislo.so
%{baseinstdir}/program/libcalclo.so
%{baseinstdir}/program/libdatelo.so
%{baseinstdir}/program/libforlo.so
%{baseinstdir}/program/libforuilo.so
%{baseinstdir}/program/libsclo.so
%{baseinstdir}/program/libscdlo.so
%{baseinstdir}/program/libscfiltlo.so
%{baseinstdir}/program/libscuilo.so
%{baseinstdir}/program/libsolverlo.so
%dir %{baseinstdir}/program/resource
%{baseinstdir}/program/resource/analysisen-US.res
%{baseinstdir}/program/resource/dateen-US.res
%{baseinstdir}/program/resource/foren-US.res
%{baseinstdir}/program/resource/foruien-US.res
%{baseinstdir}/program/resource/scen-US.res
%{baseinstdir}/program/resource/solveren-US.res
%{baseinstdir}/program/vbaobj.uno.so
%{baseinstdir}/share/registry/calc.xcd
%{baseinstdir}/program/pagein-calc
%{baseinstdir}/program/scalc
%{_datadir}/applications/libreoffice-calc.desktop
%{_bindir}/oocalc

%post calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files draw
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/help/en/sdraw.*
%{baseinstdir}/share/registry/draw.xcd
%{baseinstdir}/program/libvisioimportlo.so
%{baseinstdir}/program/pagein-draw
%{baseinstdir}/program/sdraw
%{_datadir}/applications/libreoffice-draw.desktop
%{_bindir}/oodraw

%post draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files emailmerge
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/mailmerge.py*
%{baseinstdir}/program/msgbox.py*
%{baseinstdir}/program/officehelper.py*

%files writer
%defattr(-,root,root,-)
%dir %{baseinstdir}
%{baseinstdir}/help/en/swriter.*
%dir %{baseinstdir}/program
%{baseinstdir}/program/libdoctoklo.so
%{baseinstdir}/program/libhwplo.so
%{baseinstdir}/program/liblwpftlo.so
%{baseinstdir}/program/libmswordlo.so
%if %{undefined rhel} || 0%{?rhel} >= 7
%{baseinstdir}/program/libmsworkslo.so
%endif
%{baseinstdir}/program/libooxmllo.so
%{baseinstdir}/program/libresourcemodello.so
%{baseinstdir}/program/librtftoklo.so
%{baseinstdir}/program/libswdlo.so
%{baseinstdir}/program/libswuilo.so
%{baseinstdir}/program/libt602filterlo.so
%{baseinstdir}/program/libwpftlo.so
%{baseinstdir}/program/libwriterfilterlo.so
%{baseinstdir}/program/vbaswobj.uno.so
%dir %{baseinstdir}/program/resource
%{baseinstdir}/program/resource/t602filteren-US.res
%{baseinstdir}/share/registry/writer.xcd
%{baseinstdir}/program/pagein-writer
%{baseinstdir}/program/swriter
%{_datadir}/applications/libreoffice-writer.desktop
%{_bindir}/oowriter

%post writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files impress
%defattr(-,root,root,-)
%dir %{baseinstdir}
%{baseinstdir}/help/en/simpress.*
%dir %{baseinstdir}/program
%{baseinstdir}/program/libanimcorelo.so
%{baseinstdir}/program/libplacewarelo.so
%dir %{baseinstdir}/share/config
%dir %{baseinstdir}/share/config/soffice.cfg
%dir %{baseinstdir}/share/config/soffice.cfg/simpress
%{baseinstdir}/share/config/soffice.cfg/simpress/effects.xml
%{baseinstdir}/share/config/soffice.cfg/simpress/transitions.xml
%{baseinstdir}/share/registry/impress.xcd
%{baseinstdir}/program/pagein-impress
%{baseinstdir}/program/simpress
%{_datadir}/applications/libreoffice-impress.desktop
%{_bindir}/ooimpress

%post impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files math
%defattr(-,root,root,-)
%dir %{baseinstdir}
%{baseinstdir}/help/en/smath.*
%dir %{baseinstdir}/program
%{baseinstdir}/program/libsmlo.so
%{baseinstdir}/program/libsmdlo.so
%dir %{baseinstdir}/program/resource
%{baseinstdir}/program/resource/smen-US.res
%{baseinstdir}/share/registry/math.xcd
%{baseinstdir}/program/smath
%{_datadir}/applications/libreoffice-math.desktop
%{_bindir}/oomath

%post math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files graphicfilter
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/libflashlo.so
%{baseinstdir}/program/libsvgfilterlo.so
%{baseinstdir}/share/registry/graphicfilter.xcd

%files xsltfilter
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{baseinstdir}/share/xslt
%{baseinstdir}/share/xslt/docbook
%dir %{baseinstdir}/share/xslt/export
%{baseinstdir}/share/xslt/export/uof
%{baseinstdir}/share/xslt/export/xhtml
%dir %{baseinstdir}/share/xslt/import
%{baseinstdir}/share/xslt/import/uof
%{baseinstdir}/share/registry/xsltfilter.xcd

%files javafilter
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%dir %{baseinstdir}/program/classes
%{baseinstdir}/program/classes/aportisdoc.jar
%{baseinstdir}/program/classes/pexcel.jar
%{baseinstdir}/program/classes/pocketword.jar
%{_datadir}/applications/libreoffice-javafilter.desktop
%{baseinstdir}/share/registry/palm.xcd
%{baseinstdir}/share/registry/pocketexcel.xcd
%{baseinstdir}/share/registry/pocketword.xcd

%files postgresql
%defattr(-,root,root,-)
%{baseinstdir}/program/postgresql-sdbc.uno.so
%{baseinstdir}/program/postgresql-sdbc-impl.uno.so
%{baseinstdir}/program/postgresql-sdbc.ini
%{baseinstdir}/program/services/postgresql-sdbc.rdb
%{baseinstdir}/share/registry/postgresqlsdbc.xcd

%files ure
%defattr(-,root,root,-)
%doc solver/unxlng*/bin/ure/LICENSE
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
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/libbasebmplo.so
%{baseinstdir}/program/libvclplug_svplo.so

%files pyuno
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/libpyuno.so
%{baseinstdir}/program/pythonloader.py*
%{baseinstdir}/program/pythonloader.uno.so
%{baseinstdir}/program/pythonloader.unorc
%{baseinstdir}/program/pyuno.so
%{baseinstdir}/program/wizards
%dir %{baseinstdir}/share/Scripts
%{baseinstdir}/share/Scripts/python
%{python_sitearch}/uno.py*
%{python_sitearch}/unohelper.py*
%{baseinstdir}/share/extensions/script-provider-for-python
%{baseinstdir}/share/registry/pyuno.xcd

%if %{undefined rhel}
%files kde
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/kde-open-url
%{baseinstdir}/program/kde4be1.uno.so
%{baseinstdir}/program/fps_kde4.uno.so
%{baseinstdir}/program/libvclplug_kde4lo.so
%endif

%if %{with binfilter}
%files binfilter
%defattr(-,root,root,-)
%{baseinstdir}/program/legacy_binfilters.rdb
%{baseinstdir}/program/libbf_frmlo.so
%{baseinstdir}/program/libbf_golo.so
%{baseinstdir}/program/libbf_migratefilterlo.so
%{baseinstdir}/program/libbf_ofalo.so
%{baseinstdir}/program/libbf_sblo.so
%{baseinstdir}/program/libbf_schlo.so
%{baseinstdir}/program/libbf_sclo.so
%{baseinstdir}/program/libbf_sdlo.so
%{baseinstdir}/program/libbf_smlo.so
%{baseinstdir}/program/libbf_solo.so
%{baseinstdir}/program/libbf_svtlo.so
%{baseinstdir}/program/libbf_svxlo.so
%{baseinstdir}/program/libbf_swlo.so
%{baseinstdir}/program/libbf_wrapperlo.so
%{baseinstdir}/program/libbf_xolo.so
%{baseinstdir}/program/libbindetlo.so
%{baseinstdir}/program/liblegacy_binfilterslo.so
%{baseinstdir}/program/resource/bf_frmen-US.res
%{baseinstdir}/program/resource/bf_ofaen-US.res
%{baseinstdir}/program/resource/bf_scen-US.res
%{baseinstdir}/program/resource/bf_schen-US.res
%{baseinstdir}/program/resource/bf_sden-US.res
%{baseinstdir}/program/resource/bf_smen-US.res
%{baseinstdir}/program/resource/bf_svten-US.res
%{baseinstdir}/program/resource/bf_svxen-US.res
%{baseinstdir}/program/resource/bf_swen-US.res
%{baseinstdir}/share/registry/binfilter.xcd
%{_datadir}/applications/libreoffice-binfilter.desktop
%endif

%changelog
* Mon Mar  5 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 3.5.1.2-1
- update to 3.5.1.2

* Wed Feb 29 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.1.1-2
- Resolves: rhbz#788045 swriter --help doesn't show help
- Resolves: rhbz#798667 missing .desktop icons

* Sun Feb 26 2012 David Tardon <dtardon@redhat.com> - 3.5.1.1-1
- 3.5.1 rc1
- drop 0001-Resolves-fdo-43644-survive-registered-but-unavailabl.patch
- drop 0001-Resolves-rhbz-789622-Adapt-SDK-to-changed-paths-in-L.patch
- drop 0001-Fix-fdo-45177-avoid-linked-undo-for-the-while.patch
- drop 0001-Fix-some-apparent-misuses-of-RTL_CONSTASCII_USTRINGP.patch
- drop binfilter-Fix-some-apparent-misuses-of-RTL_CONSTASCII_USTRINGP.patch
- Resolves: fdo#45177 avoid linked undo crash
- Fix some apparent misuses of RTL_CONSTASCII_USTRINGPARAM (cherry-picked from
  upstream libreoffice-3-5 branch)

* Tue Feb 14 2012 Stephan Bergmann <sbergman@redhat.com> - 3.5.0.3-5
- Resolves rhbz#789622: Adapt SDK to changed paths in LO installation

* Mon Feb 13 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.0.3-4
- ensure gdb .py files have the same timstamps so that multilib
  .pyc's and .pyo's have the same content (timestamp in binary cache)

* Sat Feb 11 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.0.3-3
- make sure .tree files don't get busted again

* Tue Feb 07 2012 Stephan Bergmann <sbergman@redhat.com> - 3.5.0.3-2
- junit4 -> junit
- Resolves: rhbz#788042 skip splashscreen with quickstarter
- with split binfilter we need fix for fdo#43644

* Thu Feb 02 2012 David Tardon <dtardon@redhat.com> - 3.5.0.3-1
- 3.5.0 rc3
- Resolves: rhbz#786328 add nlpsolver subpackage
- split legacy binary filters into subpackage

* Thu Jan 26 2012 Stephan Bergmann <sbergman@redhat.com> - 3.5.0.2-2
- add libreoffice-postgresql subpackage

* Wed Jan 25 2012 David Tardon <dtardon@redhat.com> - 3.5.0.2-1
- 3.5.0 rc2

* Thu Jan 19 2012 David Tardon <dtardon@redhat.com> - 3.5.0.1-1
- 3.5.0 rc1
- drop integrated 0001-workaround-internal-compiler-error-with-gcc-4.7.patch
- drop integrated 0001-fix-for-gcc-4.7-C-11-these-are-not-string-literal-op.patch
- drop integrated 0001-fix-for-gcc-4.7-C-11-this-is-not-string-literal-oper.patch
- drop integrated 0001-Revert-fast_merge-fix-mis-merge-of-first-module-s-st.patch
- drop integrated 0001-fix-writing-of-strings-from-the-first-module.patch
- drop integrated 0001-refactor-slightly-to-avoid-link-problems-with-gcc-4..patch

* Fri Jan 13 2012 David Tardon <dtardon@redhat.com> - 3.4.99.3-1
- 3.5.0 beta3
- drop integrated 0001-fix-syntactic-error.patch
- drop integrated 0001-gcc-trunk-fix-error-unable-to-find-string-literal-op.patch
- drop integrated 0001-gcc-trunk-avoid-confusion.patch
- drop integrated 0001-workaround-for-LO-namespace-pollution-breaking-KDE4-.patch
- drop integrated 0001-smath-does-not-handle-accents-in-MathML.patch
- Resolves: rhbz#533318 smath does not handle accents in MathML
- Resolves: rhbz#771108 English menu in writer despite installation of
  libreoffice-langpack-de

* Fri Jan 06 2012 David Tardon <dtardon@redhat.com> - 3.4.99.2-2
- rebuild with gcc 4.7

* Wed Dec 21 2011 David Tardon <dtardon@redhat.com> - 3.4.99.2-1
- 3.5.0 beta2
- drop integrated 0001-Resolves-rhbz-761009-IFSD_Equal-is-asymmetrical.patch
- drop integrated 0001-Resolves-rhbz-767708-avoid-SIGBUS-writing-to-overcom.patch
- drop integrated 0001-force-gbuild-stage-for-CustomTargets.patch
- drop integrated 0001-these-translations-do-already-exist-in-translations-.patch
- drop integrated 0001-Fix-typo-and-clean-up.patch
- use system mysql-connector-c++

* Sun Dec 18 2011 David Tardon <dtardon@redhat.com> - 3.4.99.1-1
- 3.5.0 beta1
- drop integrated 0001-Related-fdo-37195-migrationoo3-not-registered.patch
- drop integrated 0001-Related-i58612-don-t-crash-anyway.patch
- drop integrated 0001-Related-rhbz-652604-better-survive-exceptions-thrown.patch
- drop integrated 0001-Related-rhbz-702833-addEventListener-without-removeE.patch
- drop integrated 0001-Related-rhbz-711087-band-aid.patch
- drop integrated 0001-Related-rhbz-718976-crash-in-SwTxtSizeInfo-GetMultiC.patch
- drop integrated 0001-Related-rhbz-730225-avoid-segv-in-ld-this-was-set-to.patch
- drop integrated 0001-Related-rhbz-753201-fedora-ant-java-1.5.0-gcj-won-t-.patch
- drop integrated 0001-Resolves-fdo-32665-handle-that-FreeSerif-lacks-some-.patch
- drop integrated 0001-Resolves-rhbz-693265-fix-crash-from-unhandled-except.patch
- drop integrated 0001-Resolves-rhbz-695509-crash-in-RefreshDocumentLB.patch
- drop integrated 0001-Resolves-rhbz-713154-pdf-export-dialog-too-tall-to-f.patch
- drop integrated 0001-Resolves-rhbz-715549-use-fontconfig-s-detected-forma.patch
- drop integrated 0001-Resolves-rhbz-738255-avoid-crash-on-NULL-pointer.patch
- drop integrated 0001-Resolves-rhbz-751290-KDE-black-on-dark-tooltips.patch
- drop integrated 0001-add-Oracle-Java-1.7.0-recognition.patch
- drop integrated 0001-avoid-using-com.sun.org-apis.patch
- drop integrated 0001-bubble-down-configure-test-findings-on-visibility.patch
- drop integrated 0001-fix-horizontal-scrollbars-with-KDE-oxygen-style-bnc-.patch
- drop integrated 0001-gtk3-fix-cairo-canvas-crash-for-non-X-or-svp-backend.patch
- drop integrated 0001-helgrind-Related-rhbz-655686-get-order-of-shutdown-c.patch
- drop integrated 0001-rhbz-667082-do-not-crash-importing-section-containin.patch
- drop integrated 0001-rhbz-702635-set-correct-page-number-when-exporting-s.patch
- drop integrated Backport-reading-AES-encrypted-ODF-1.2-documents.patch
- drop integrated gdb-pretty-printers.patch
- drop integrated kde4configure.patch
- drop integrated libreoffice-ppc64.patch
- drop integrated openoffice.org-3.3.0.ooo108637.sfx2.uisavedir.patch
- drop integrated openoffice.org-3.3.0.ooo113273.desktop.resolvelinks.patch
- drop integrated vbahelper.visibility.patch
- drop libreoffice-testtools subpackage, because testtool has been
  removed by upstream

* Thu Dec 15 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-6
- Resolves: rhbz#761009 IFSD_Equal is asymmetrical
- Resolves: rhbz#767708 write to mmap'ed file w/o disk space: SIGBUS

* Tue Nov 29 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-5
- Resolves: rhbz#757653 fix headless crash with cairo canvas

* Tue Nov 22 2011 Lukas Tinkl <ltinkl@redhat.com> - 3.4.4.2-4
- Resolves: rhbz#751290 - [kde] LibreOffice has black on dark-grey tooltip-texts

* Fri Nov 11 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-3
- Related: fdo#42534 0001-Related-i58612-don-t-crash-anyway.patch
- Resolves: fdo#42749 KDE oxygen theme and scrollbars

* Thu Nov 10 2011 Stephan Bergmann <sbergman@redhat.com> - 3.4.4.2-2
- Patch to backport reading AES-encrypted ODF 1.2 documents

* Thu Nov 03 2011 David Tardon <dtardon@redhat.com> - 3.4.4.2-1
- 3.4.4 rc2

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 1:3.4.4.1-4
- rebuild(poppler)

* Thu Oct 27 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.1-3
- Resolves: rhbz#665800 missing glyph symbol shown when toggling bold/italic
  for Sinhala text

* Thu Oct 27 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.1-2
- possible fix for java 1.7.0 detection


* Wed Oct 26 2011 David Tardon <dtardon@redhat.com> - 3.4.4.1-1
- 3.4.4 rc1

* Tue Oct 25 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-16
- allow building with gcj

* Fri Oct 21 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-15
- Resolves: rhbz#747356 let Qt call XInitThreads
- fix .sdw import

* Wed Oct 19 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-14
- Related: rhbz#743750 addXineramaScreenUnique issue
 
* Fri Oct 07 2011 Stephan Bergmann <sbergman@redhat.com> - 3.4.3.2-13
- Patches to build with GCC 6.4.1

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 3.4.3.2-12
- Rebuild (poppler-0.18.0)

* Tue Sep 20 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-11
- Resolves: rhbz#738133 fix bn discard string
- Resolves: fdo#35513 avoid crash while processing incorrect print range

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 3.4.3.2-10
- Rebuild (poppler-0.17.3)

* Thu Sep 15 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-9
- Resolves: rhbz#738255 avoid crash on sc inputhdl

* Tue Sep 13 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-8
- Resolves: rhbz#274631 remove NoDisplay from -math.desktop

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
