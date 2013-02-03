Summary:	GGZ Gaming Zone - KDE frontends and clients
Summary(pl.UTF-8):	GGZ Gaming Zone - interfejsy i klienci KDE
Name:		ggz-kde-client
Version:	0.0.14.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://mirrors.dotsrc.org/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b6218d3e0e5c64757669150f0a7664d4
URL:		http://www.ggzgamingzone.org/
BuildRequires:	gettext-devel
BuildRequires:	ggz-client-libs-devel >= 0.0.14
BuildRequires:	howl-devel
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	libggz-devel >= 0.0.14
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3
Requires:	ggz-client-libs >= 0.0.14
Requires:	kdelibs >= 3
Requires:	libggz >= 0.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GGZ Gaming Zone - KDE frontends and clients.

%description -l pl.UTF-8
GGZ Gaming Zone - interfejsy i klienci KDE.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# library is noinst, so API docs are useless
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ggzcore++

# po: kggz, compcal, ggzap, kcm_ggz, kgrubby, shadowbridge
# khtml: kggz, kioslave/ggz, kioslave/ggzmeta
%find_lang kggz --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kggz.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart.GGZ README* TODO
%attr(755,root,root) %{_bindir}/compcal
%attr(755,root,root) %{_bindir}/keepalivecontrol
%attr(755,root,root) %{_bindir}/kggz
%attr(755,root,root) %{_bindir}/kgrubby
%attr(755,root,root) %{_bindir}/ggzap
%attr(755,root,root) %{_bindir}/shadowbridge
%attr(755,root,root) %{_libdir}/kde3/libkcm_ggz.so
%{_libdir}/kde3/libkcm_ggz.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_ggz_default.so
%{_libdir}/kde3/libkcm_ggz_default.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_ggz_metaserver.so
%{_libdir}/kde3/libkcm_ggz_metaserver.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_ggz_ggzd.so
%{_libdir}/kde3/libkcm_ggz_ggzd.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_ggz_games.so
%{_libdir}/kde3/libkcm_ggz_games.la
%attr(755,root,root) %{_libdir}/kde3/libkio_ggz.so
%{_libdir}/kde3/libkio_ggz.la
%attr(755,root,root) %{_libdir}/kde3/libkio_ggzmeta.so
%{_libdir}/kde3/libkio_ggzmeta.la
%{_datadir}/apps/compcal
%{_datadir}/apps/keepalivecontrol
%{_datadir}/apps/kggz
%{_datadir}/apps/kgrubby
%{_datadir}/config/compcalrc
%{_datadir}/config/kggzrc
%{_datadir}/services/ggz.protocol
%{_datadir}/services/ggzmeta.protocol
%{_desktopdir}/compcal.desktop
%{_desktopdir}/ggzap.desktop
%{_desktopdir}/kcmggz.desktop
%{_desktopdir}/keepalivecontrol.desktop
%{_desktopdir}/kggz.desktop
%{_desktopdir}/kgrubby.desktop
%{_desktopdir}/shadowbridge.desktop
%{_mandir}/man6/compcal.6*
%{_mandir}/man6/ggzap.6*
%{_mandir}/man6/keepalivecontrol.6*
%{_mandir}/man6/kggz.6*
%{_mandir}/man6/kgrubby.6*
%{_mandir}/man6/shadowbridge.6*
