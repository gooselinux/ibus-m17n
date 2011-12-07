%define require_ibus_version 1.3.0

Name:       ibus-m17n
Version:    1.3.0
Release:    1%{?dist}
Summary:    The M17N engine for IBus platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz

Patch0:     ibus-m17n-iok.patch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  m17n-lib-devel
BuildRequires:  ibus-devel >= %{require_ibus_version}

Requires:   ibus >= %{require_ibus_version}
Requires:   m17n-lib
Requires:   iok > 1.3.1

%description
M17N engine for IBus input platform. It allows input of many languages using
the input table maps from m17n-db.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_datadir}/ibus-m17n
%{_libexecdir}/ibus-engine-m17n
%{_datadir}/ibus/component/*

%changelog
* Mon Mar 29 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.0-1
- Update to 1.3.0.
- Update iok patch.
- Fix bug 577148 - IOK screen appears with all keyboard layouts on ibus language panel

* Tue Feb 02 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100202-1
- Update to 1.2.99.20100202.
- Update iok patch.

* Thu Dec 17 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20091217-1
- Update to 1.2.0.20091217.
- Update iok patch.

* Fri Nov 20 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20091120-1
- Update to 1.2.0.20091120.
- Fix bug 530976

* Fri Oct 23 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090617-5
- Update iok patch to fix bug 530493.

* Wed Oct 14 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090617-4
- Update iok patch to fix build error.

* Tue Oct 13 2009 Parag <pnemade@redhat.com> - 1.2.0.20090617-3
- Re-enable iok support to ibus-m17n.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090617-1
- Update to 1.2.0.20090617.

* Thu Mar 05 2009 Parag <pnemade@redhat.com> - 1.1.0.20090211-4
- Add iok support to ibus-m17n.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.20090211-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090211-2
- Add patch ibus-m17n-HEAD.patch from upstream git tree.
- Make Control + Alt + ... available. (#482789)

* Wed Feb 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090211-1
- Update to 1.1.0.20090211.

* Thu Feb 05 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090205-1
- Update to 1.1.0.20090205.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20081013-4
- Rebuild for Python 2.6

* Thu Oct 16 2008 Jens Petersen <petersen@redhat.com> - 0.1.1.20081013-3
- move the .engine files to m17n-db and m17n-contrib (#466410)

* Wed Oct 15 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081013-2
- Move unicode, rfc1345 to generic package, and syrc-phonetic to syriac package.

* Mon Oct 13 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081013-1
- Update to 0.1.1.20081013.

* Thu Oct 09 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081009-1
- Update to 0.1.1.20081009.

* Mon Sep 01 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update to 0.1.1.20080901.

* Sat Aug 23 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080823-1
- Update to 0.1.1.20080823.

* Fri Aug 15 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080815-1
- Update to 0.1.1.20080815.

* Tue Aug 12 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080812-1
- Update to 0.1.1.20080812.

* Thu Aug 07 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.0.20080810-1
- The first version.
