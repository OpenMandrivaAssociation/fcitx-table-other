Summary:	Other tables for Fcitx
Name:		fcitx-table-other
Version:	0.2.3
Release:	1
Group:		System/Internationalization
License:	GPLv3+
URL:		https://fcitx-im.org/wiki/Fcitx
Source0:	http://download.fcitx-im.org/fcitx-table-other/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	pkgconfig(fcitx)
BuildRequires:	gettext
BuildRequires:	intltool
BuildArch:	noarch
Requires:	fcitx

%description
Fcitx-table-other is a fork of ibus-table-others for Fcitx,
provides additional tables.

%prep
%setup -q

%build
# (tpg) building in a clean dir fails
%cmake .
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/fcitx/table/*.mb
%{_datadir}/fcitx/table/*.conf
%{_datadir}/fcitx/imicon/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
