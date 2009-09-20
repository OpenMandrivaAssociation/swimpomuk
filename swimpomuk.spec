%define svnrev 112

Name:		swimpomuk
Version:	0.1
Release:	%mkrel 0.%{svnrev}.2
Source:		%{name}-svn%{svnrev}.tar.bz2
BuildRequires:	cmake kdelibs4-devel nepomuk-kde-devel kdebase4-devel kde4-macros
URL:		http://nepomuk.linbox.org/
License:	LGPLv2
Group:		Graphical desktop/KDE
Summary:	KDE client for SWIM
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
SwimpomuK is a KDE client for the Mandriva issue and support forum server                                                   
(SWIM). It allows to annotate, relate, and query issues and forum entries, thus                                              
improving the way users deal with their daily Linux problems.

%prep
%setup -q -n %{name}-svn%{svnrev}

%build
#cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix}
%cmake_kde4
%make

%install
rm -fr %buildroot
make -C build DESTDIR=%buildroot install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_kde_bindir}/bugger
%{_kde_bindir}/linobrowser
%{_kde_libdir}/kde4/konq_swimsidebar.so
%{_kde_libdir}/kde4/nepomuk_linohardwareannotationplugin.so
%{_kde_libdir}/kde4/nepomuk_linosoftwareannotationplugin.so
%{_kde_libdir}/libkdeinit4_bugger.so
%{_kde_applicationsdir}/bugger.desktop
%{_kde_applicationsdir}/linobrowser.desktop
%{_kde_appsdir}/konqsidebartng/entries/swimsidebar.desktop
%{_kde_appsdir}/linobrowser/linobrowserui.rc
%{_kde_appsdir}/nepomuk/ontologies/lino.desktop
%{_kde_appsdir}/nepomuk/ontologies/lino.trig
%{_kde_appsdir}/nepomuk/ontologies/wf.desktop
%{_kde_appsdir}/nepomuk/ontologies/wf.n3
%{_kde_datadir}/config.kcfg/lino.kcfg
%{_kde_services}/nepomukannotationplugins/linohardwareannotationplugin.desktop
%{_kde_services}/nepomukannotationplugins/linosoftwareannotationplugin.desktop
