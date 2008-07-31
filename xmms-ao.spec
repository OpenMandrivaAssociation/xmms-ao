%define name xmms-ao
%define tarball_name xmmsao
%define version 0.7
%define release %mkrel 5

Summary:		Output plugin for xmms using libao2
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source:			%{tarball_name}-%{version}.tar.bz2
License:		GPL
Group:			Sound
Requires:		xmms
BuildRequires:		xmms-devel, libao-devel, gtk+-devel
BuildRoot:		%{_tmppath}/%{name}-buildroot
Obsoletes:		xmmsao <= 0.6
Provides:		xmmsao > 0.6

%description
An xmms output plugin that uses the ao audio output library.  The great
benefit of this is that, whether your sound system is OSS, ALSA, ESD, or
aRts, the sound will work.  You can (pressing stop in-between) switch among
those, and the plugin will adapt.  It is ideal for users who switch regularly
between desktop environments or for admins who are tired of fielding "why
doesn't xmms-esd work in KDE?" questions.

xmms-ao should support most effect plugins.  As this plugin outputs to a
generic library, an output plugin which operates closer to the actual output
system may be preferable in some cases.

%prep
%setup

%build
%make CC="gcc -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/xmms/Output
cp libaoout.so $RPM_BUILD_ROOT/%{_libdir}/xmms/Output

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,0755)
%doc COPYING
%{_libdir}/xmms/Output/libaoout.so

