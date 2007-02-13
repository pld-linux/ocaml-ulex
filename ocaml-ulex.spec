Summary:	Lexer generator for Unicode and OCaml
Summary(pl.UTF-8):	Lexer dla OCamla i Unicode
Name:		ocaml-ulex
Version:	0.8
Release:	2
License:	MIT
Group:		Development/Tools
Source0:	http://www.cduce.org/download/ulex-%{version}.tar.gz
# Source0-md5:	baf9fe9fc381c7824a2e0e368da5fa13
BuildRequires:	ocaml >= 3.09.0
BuildRequires:	ocaml-findlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ulex is a lexer generator for Unicode and OCaml.

%description -l pl.UTF-8
ulex jest lexerem dla OCamla i Unicode.

%prep
%setup -q -n ulex-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ulex

%{__make} install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

echo 'directory = "+ulex"' \
	>> $RPM_BUILD_ROOT%{_libdir}/ocaml/ulex/META
mv -f $RPM_BUILD_ROOT%{_libdir}/ocaml/ulex/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ulex/META

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/ocaml/ulex
%{_libdir}/ocaml/ulex/*.cm*
%{_libdir}/ocaml/site-lib/ulex
