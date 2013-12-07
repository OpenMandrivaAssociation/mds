#%#define _use_internal_dependency_generator	0
%define __noautoreq 'pear\\(graph|pear\\(includes|pear\\(modules'

%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Mandriva Management Directory Server
Name:		mds
Version:	2.4.2.2
Release:	5
License:	GPLv2
Group:		System/Servers
Url:		http://mds.mandriva.org
Source0:	http://mds.mandriva.org/pub/mds/sources/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(python)

%description
The Mandriva Management Directory Server.

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
%if %mdkversion >= 201200 && %{_use_internal_dependency_generator}
# add buggy self dependencies
Provides:	pear(edit.php)
Provides:	pear(mail-xmlrpc.php)
Provides:	pear(mail.inc.php)
%endif

%description -n	mmc-web-mail
Mandriva Management Console web interface designed by Linbox.

This is the Mail module.

%package -n	mmc-web-network
Summary:	DNS/DHCP management module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3
%if %mdkversion >= 201200 && %{_use_internal_dependency_generator}
# add buggy self dependencies
Provides:	pear(localSidebar.php)
Provides:	pear(servicedhcpfailover.php)
Provides:	pear(subnetedit.php)
%endif

%description -n	mmc-web-network
Mandriva Management Console web interface designed by Linbox.

This is the Network module.

%package -n	mmc-web-proxy
Summary:	SquidGuard module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3
%if %mdkversion >= 201200 && %{_use_internal_dependency_generator}
# add buggy self dependencies
Provides:	pear(localSidebar.php)
%endif

%description -n	mmc-web-proxy
Mandriva Management Console web interface designed by Linbox.

This is the Squid/SquidGuard module.

%package -n	mmc-web-samba
Summary:	SAMBA module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3
%if %mdkversion >= 201200 && %{_use_internal_dependency_generator}
# add buggy self dependencies
Provides:	pear(user-xmlrpc.inc.php)
%endif

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
%if %mdkversion >= 201200 && %{_use_internal_dependency_generator}
# add buggy self dependencies
Provides:	pear(sshlpk-xmlrpc.php)
%endif

%description -n	mmc-web-sshlpk
Mandriva Management Console web interface designed by Linbox.

This is the SSH public key module.

%package -n	mmc-web-userquota
Summary:	User quota module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.3
%if %mdkversion >= 201200 && %{_use_internal_dependency_generator}
# add buggy self dependencies
Provides:	pear(userquota-xmlrpc.php)
Provides:	pear(userquota.php)
%endif

%description -n	mmc-web-userquota
Mandriva Management Console web interface designed by Linbox.

This is the userquota module.

%prep
%setup -q

%build
%configure
make

%install
make DESTDIR="%{buildroot}" install
# cleanup
rm -f `find %{buildroot} -name *.pyo`
%find_lang mail
%find_lang network
%find_lang proxy
%find_lang samba
%find_lang bulkimport
%find_lang sshlpk
%find_lang userquota

%files -n python-mmc-mail
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/mail.ini
%{py_puresitedir}/mmc/plugins/mail

%files -n python-mmc-network
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/network.ini
%{py_puresitedir}/mmc/plugins/network

%files -n python-mmc-proxy
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/proxy.ini
%{py_puresitedir}/mmc/plugins/proxy

%files -n python-mmc-samba
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/samba.ini
%{py_puresitedir}/mmc/plugins/samba
%{_libdir}/mmc/add_machine_script
%{_libdir}/mmc/add_change_share_script
%{_libdir}/mmc/add_printer_script
%{_libdir}/mmc/delete_printer_script
%{_libdir}/mmc/delete_share_script

%files -n python-mmc-bulkimport
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/bulkimport.ini
%{py_puresitedir}/mmc/plugins/bulkimport

%files -n python-mmc-sshlpk
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/sshlpk.ini
%{py_puresitedir}/mmc/plugins/sshlpk

%files -n python-mmc-userquota
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/userquota.ini
%{py_puresitedir}/mmc/plugins/userquota

%files -n mmc-web-mail -f mail.lang
%dir %{_datadir}/mmc/modules/mail
%dir %{_datadir}/mmc/modules/mail/locale
%{_datadir}/mmc/modules/mail/*.php
%{_datadir}/mmc/modules/mail/aliases
%{_datadir}/mmc/modules/mail/domains
%{_datadir}/mmc/modules/mail/graph
%{_datadir}/mmc/modules/mail/includes

%files -n mmc-web-network -f network.lang
%dir %{_datadir}/mmc/modules/network
%dir %{_datadir}/mmc/modules/network/locale
%{_datadir}/mmc/modules/network/*.php
%{_datadir}/mmc/modules/network/dhcplogview
%{_datadir}/mmc/modules/network/dnslogview
%{_datadir}/mmc/modules/network/graph
%{_datadir}/mmc/modules/network/includes
%{_datadir}/mmc/modules/network/network

%files -n mmc-web-proxy -f proxy.lang
%dir %{_datadir}/mmc/modules/proxy
%dir %{_datadir}/mmc/modules/proxy/locale
%{_datadir}/mmc/modules/proxy/*.php
%{_datadir}/mmc/modules/proxy/blacklist
%{_datadir}/mmc/modules/proxy/graph
%{_datadir}/mmc/modules/proxy/includes

%files -n mmc-web-samba -f samba.lang
%dir %{_datadir}/mmc/modules/samba
%dir %{_datadir}/mmc/modules/samba/locale
%{_datadir}/mmc/modules/samba/*.php
%{_datadir}/mmc/modules/samba/config
%{_datadir}/mmc/modules/samba/includes
%{_datadir}/mmc/modules/samba/machines
%{_datadir}/mmc/modules/samba/shares
%{_datadir}/mmc/modules/samba/status
%{_datadir}/mmc/modules/samba/views

%files -n mmc-web-bulkimport -f bulkimport.lang
%dir %{_datadir}/mmc/modules/bulkimport
%dir %{_datadir}/mmc/modules/bulkimport/locale
%{_datadir}/mmc/modules/bulkimport/*.php
%{_datadir}/mmc/modules/bulkimport/import
%{_datadir}/mmc/modules/bulkimport/includes

%files -n mmc-web-sshlpk -f sshlpk.lang
%dir %{_datadir}/mmc/modules/sshlpk
%dir %{_datadir}/mmc/modules/sshlpk/locale
%{_datadir}/mmc/modules/sshlpk/*.php
%{_datadir}/mmc/modules/sshlpk/includes

%files -n mmc-web-userquota -f userquota.lang
%dir %{_datadir}/mmc/modules/userquota
%dir %{_datadir}/mmc/modules/userquota/locale
%{_datadir}/mmc/modules/userquota/*.php
%{_datadir}/mmc/modules/userquota/includes

