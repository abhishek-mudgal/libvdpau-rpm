Name:		libvdpau
Version:        1.1.1
Release:        1
Summary:        Generate Your Projects
Group:          Development/Libraries
License:        Custom
URL:            https://www.freedesktop.org/wiki/Software/VDPAU
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
Requires:       libxext


%description
VDPAU is the Video Decode and Presentation API for UNIX. It provides an interface to video decode acceleration and presentation hardware present in modern GPUs.

%prep
%setup -q -n %{name}-%{version}/libvdpau

%build
./autogen.sh
%configure \
                --enable-static
make %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)
%{_libdir}/libvdpau/*.so
%{_libdir}/libvdpau/*.so.*
