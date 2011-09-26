%define _requires_exceptions pear(graph\\|pear(includes\\|pear(modules

%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%if %mdkversion < 200610
%define py_puresitedir %{_prefix}/lib/python%{pyver}/site-packages/
%endif

Summary:	Mandriva Management Directory Server
Name:		mds
Version:	2.4.2
%define subrel 1
Release:	%mkrel 0
License:	GPL
Group:		System/Servers
URL:		http://mds.mandriva.org/
Source0:	http://mds.mandriva.org/pub/mds/sources/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  gettext-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Mandriva Management Directory Server (src.rpm)

%package -n	python-mmc-samba
Summary:	Mandriva Management Console SAMBA plugin
Group:		System/Servers
Requires:	acl
Requires:	pylibacl
Requires:	python-mmc-base >= 3.0.3
Requires:	python-smbpasswd
Requires:	samba-common

%description -n	python-mmc-samba
SAMBA management plugin for the MMC. It includes
SAMBA accounts and shares management.

%package -n	python-mmc-mail
Summary:	Mandriva Management Console base plugin
Group:		System/Servers
Suggests:	postfix
Suggests:	postfix-ldap
Requires:	python-mmc-base >= 3.0.3

%description -n	python-mmc-mail
Mail account management plugin for the MMC.

%package -n	python-mmc-proxy
Summary:	Mandriva Management Console proxy plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.3
Requires:	squid
Requires:	squidGuard

%description -n	python-mmc-proxy
Squidguard/Squid management plugin for the MMC.

%package -n	python-mmc-network
Summary:	Mandriva Management Console network plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.3
Suggests:	dhcp-server
Suggests:   	bind

%description -n	python-mmc-network
DNS/DHCP management plugin for the MMC.

This plugin requires a LDAP-patched version of ISC DHCPD and BIND9.

%package -n	python-mmc-bulkimport
Summary:	Mandriva Management Console bulkimport plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.3

%description -n	python-mmc-bulkimport
Mass import plugin for MMC.

The bulkimport plugin can be used to import or modify multiple
users with CSV files.

%package -n	python-mmc-sshlpk
Summary:	Mandriva Management Console sshlpk plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.3

%description -n	python-mmc-sshlpk
MMC agent SSH public key plugin.

This plugin allows to add SSH public keys to LDAP user entries.
These keys can then be retrieved by OpenSSH with the LDAP Public Key patch. See
http://code.google.com/p/openssh-lpk/

%package -n	python-mmc-userquota
Summary:	Mandriva Management Console userquota plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.3
Requires:	quota

%description -n	python-mmc-userquota
MMC quota plugin.

This plugin allows to add user quota on filesystem. It also provide a ldap
attribute for network quotas.

%package -n	mmc-web-mail
Summary:	Postfix/Mail module for the MMC web interface
Group:		System/Servers
Requires:	postfix
Requires:	mmc-web-base >= 3.0.3

%description -n	mmc-web-mail
Mandriva Management Console web interface designed by Linbox.

This is the Mail module.

%package -n	mmc-web-network
Summary:	DNS/DHCP management module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3

%description -n	mmc-web-network
Mandriva Management Console web interface designed by Linbox.

This is the Network module.

%package -n	mmc-web-proxy
Summary:	SquidGuard module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3

%description -n	mmc-web-proxy
Mandriva Management Console web interface designed by Linbox.

This is the Squid/SquidGuard module.

%package -n	mmc-web-samba
Summary:	SAMBA module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3

%description -n	mmc-web-samba
Mandriva Management Console web interface designed by Linbox.

This is the SAMBA module.

%package -n	mmc-web-bulkimport
Summary:	Bulk import module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3

%description -n	mmc-web-bulkimport
Mandriva Management Console web interface designed by Linbox.

This is the bulk import module.

%package -n	mmc-web-sshlpk
Summary:	SSH public key module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3

%description -n	mmc-web-sshlpk
Mandriva Management Console web interface designed by Linbox.

This is the SSH public key module.

%package -n	mmc-web-userquota
Summary:	User quota module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3

%description -n	mmc-web-userquota
Mandriva Management Console web interface designed by Linbox.

This is the userquota module.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
rm -rf %{buildroot}
make DESTDIR="$RPM_BUILD_ROOT" install
# cleanup
rm -f `find %{buildroot} -name *.pyo`
%find_lang mail
%find_lang network
%find_lang proxy
%find_lang samba
%find_lang bulkimport
%find_lang sshlpk
%find_lang userquota

%clean
rm -rf %{buildroot}

%files -n python-mmc-mail
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/mmc
%dir %{_sysconfdir}/mmc/plugins
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/mail.ini
%dir %{py_puresitedir}/mmc
%dir %{py_puresitedir}/mmc/plugins
%{py_puresitedir}/mmc/plugins/mail

%files -n python-mmc-network
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/mmc
%dir %{_sysconfdir}/mmc/plugins
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/network.ini
%dir %{py_puresitedir}/mmc
%dir %{py_puresitedir}/mmc/plugins
%{py_puresitedir}/mmc/plugins/network

%files -n python-mmc-proxy
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/mmc
%dir %{_sysconfdir}/mmc/plugins
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/proxy.ini
%dir %{py_puresitedir}/mmc
%dir %{py_puresitedir}/mmc/plugins
%{py_puresitedir}/mmc/plugins/proxy

%files -n python-mmc-samba
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/mmc
%dir %{_sysconfdir}/mmc/plugins
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/samba.ini
%dir %{py_puresitedir}/mmc
%dir %{py_puresitedir}/mmc/plugins
%{py_puresitedir}/mmc/plugins/samba
%dir %{_libdir}/mmc
%{_libdir}/mmc/add_machine_script
%{_libdir}/mmc/add_change_share_script
%{_libdir}/mmc/add_printer_script
%{_libdir}/mmc/delete_printer_script
%{_libdir}/mmc/delete_share_script

%files -n python-mmc-bulkimport
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/mmc
%dir %{_sysconfdir}/mmc/plugins
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/bulkimport.ini
%dir %{py_puresitedir}/mmc
%dir %{py_puresitedir}/mmc/plugins
%{py_puresitedir}/mmc/plugins/bulkimport

%files -n python-mmc-sshlpk
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/mmc
%dir %{_sysconfdir}/mmc/plugins
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/sshlpk.ini
%dir %{py_puresitedir}/mmc
%dir %{py_puresitedir}/mmc/plugins
%{py_puresitedir}/mmc/plugins/sshlpk

%files -n python-mmc-userquota
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/mmc
%dir %{_sysconfdir}/mmc/plugins
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/userquota.ini
%dir %{py_puresitedir}/mmc
%dir %{py_puresitedir}/mmc/plugins
%{py_puresitedir}/mmc/plugins/userquota

%files -n mmc-web-mail -f mail.lang
%defattr(-,root,root,0755)
%dir %{_datadir}/mmc
%dir %{_datadir}/mmc/modules
%{_datadir}/mmc/modules/mail

%files -n mmc-web-network -f network.lang
%defattr(-,root,root,0755)
%dir %{_datadir}/mmc
%dir %{_datadir}/mmc/modules
%{_datadir}/mmc/modules/network

%files -n mmc-web-proxy -f proxy.lang
%defattr(-,root,root,0755)
%dir %{_datadir}/mmc
%dir %{_datadir}/mmc/modules
%{_datadir}/mmc/modules/proxy

%files -n mmc-web-samba -f samba.lang
%defattr(-,root,root,0755)
%dir %{_datadir}/mmc
%dir %{_datadir}/mmc/modules
%{_datadir}/mmc/modules/samba

%files -n mmc-web-bulkimport -f bulkimport.lang
%defattr(-,root,root,0755)
%dir %{_datadir}/mmc
%dir %{_datadir}/mmc/modules
%{_datadir}/mmc/modules/bulkimport

%files -n mmc-web-sshlpk -f sshlpk.lang
%defattr(-,root,root,0755)
%dir %{_datadir}/mmc
%dir %{_datadir}/mmc/modules
%{_datadir}/mmc/modules/sshlpk

%files -n mmc-web-userquota -f userquota.lang
%defattr(-,root,root,0755)
%dir %{_datadir}/mmc
%dir %{_datadir}/mmc/modules
%{_datadir}/mmc/modules/userquota
