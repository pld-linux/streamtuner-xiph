Summary:	Plugin for streamtuner implementing a dir.xiph.org handler
Summary(pl):	Wtyczka dla streamtunera implementuj±ca obs³ugê dir.xiph.org
Name:		streamtuner-xiph
Version:	0.1.0
Release:	1
License:	Free
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/streamtuner/%{name}-%{version}.tar.gz
# Source0-md5:	07e06b4737a9949399222333f56b7659
URL:		http://www.nongnu.org/streamtuner/
Buildrequires:	gtk+2-devel >= 2:2.4.4
Buildrequires:	streamtuner-devel >= 0.12.0
Requires:	streamtuner >= 0.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for streamtuner implementing a dir.xiph.org handler.

%description -l pl
Wtyczka dla streamtunera implementuj±ca obs³ugê dir.xiph.org.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/streamtuner/plugins/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/streamtuner/plugins/*.so
