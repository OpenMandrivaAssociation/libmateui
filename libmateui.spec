%define api	2
%define major	0
%define libname	%mklibname mateui %{api} %{major}
%define devname	%mklibname -d mateui

Summary:	Main MATE libraries
Name:		libmateui
Version:	1.4.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libmate-2.0)
BuildRequires:	pkgconfig(libmatecanvas-2.0)
BuildRequires:	pkgconfig(libmatecomponent-2.0)
BuildRequires:	pkgconfig(libmatecomponentui-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-keyring-1)
BuildRequires:	pkgconfig(mate-vfs-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)

Requires: libmatecomponentui
Requires: mate-icon-theme

%description
Data files for the MATE UI library such as translations.

%package -n %{libname}
Summary:	MATE libraries
Group:		%{group}

%description -n %{libname}
MATE library contains extra widgets to let your 
MATE applications really shine

%package -n %{devname}
Summary:	Development libraries, include files for MATE
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development library, headers files and documentation needed in order 
to develop applications using the MATE library.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README 
%{_libdir}/libglade/2.0/*.so
%{_datadir}/pixmaps/*

%files -n %{libname}
%{_libdir}/libmateui-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so



%changelog
* Wed Aug 01 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811525
- new version 1.4.0

* Wed Jun 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-3
+ Revision: 805469
- rebuild adding require for libmatecomponentui

* Mon Jun 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 802481
- rebuild
- imported package libmateui

