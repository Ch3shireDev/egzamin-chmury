# Odpowiedzi

## Rozdział 1. Chmura obliczeniowa — podstawowe pojęcia

1. Jakiego rodzaju chmura wymaga posiadania łącza internetowego i pozwala każdemu użytkownikowi korzystać z jej usług?
   Odpowiedź: publiczna
2. Jaki model usług daje największą kontrolę nad zasobami?
   Odpowiedź: IaaS
3. W jakim modelu usług zarządzanie infrastrukturą jest najprostsze?
   Odpowiedź: SaaS
4. Jaki model usług oferuje najnowsze funkcjonalności i aktualizacje?
   Odpowiedź: PaaS
5. Co decyduje o izolowaniu środowisk klientów w chmurze Azure?
   Odpowiedź: usługa Azure Fabric
6. Jak nazywa się pierwszy poziom dostępu w chmurze Microsoft Azure?
   Odpowiedź: podmiot
7. Jaki jest najniższy poziom szczegółowości dostępu do zasobów?
   Odpowiedź: zasób
8. Jaki jest zalecany poziom szczegółowości dostępu do zasobów Azure?
   Odpowiedź: grupa zasobów
9. Jaki jest system naliczania opłat w chmurze Azure?
   Odpowiedź: minutowy
10. Częścią jakiego modelu są szablony ARM?
    Odpowiedź: IaC

## Rozdział 2. Sieci — podstawa modelu IaaS

1. Jaki model usług wykorzystuje sieć Azure?
   Odpowiedź: obie powyższe odpowiedzi są poprawne
2. Co definiuje zakres adresów IP?
   Odpowiedź: CIDR
3. Jakie usługi są dołączane do sieci wirtualnej za pomocą punktów końcowych?
   Odpowiedź: PaaS
4. Domyślnym serwerem DNS w chmurze Azure jest:
   Odpowiedź: serwer Azure DNS
5. Kiedy można tworzyć punkty usług?
   Odpowiedź: w dowolnym momencie
6. Prywatny adres IP w sieci Azure jest:
   Odpowiedź: dynamiczny lub statyczny
7. Publiczny adres IP w sieci Azure jest:
   Odpowiedź: dynamiczny lub statyczny
8. Sieciowa grupa zabezpieczeń to:
   Odpowiedź: zbiór reguł bezpieczeństwa kontrolujących przepływ ruchu
9. Co definiuje sieciowa grupa zabezpieczeń?
   Odpowiedź: obie powyższe odpowiedzi są poprawne
10. Do jakiego zasobu można przypisać sieciową grupę zabezpieczeń?
    Odpowiedź: sieci wirtualnej

## Rozdział 3. Infrastruktura jako usługa — pierwsza warstwa chmury obliczeniowej

1. Jaka jest najstarsza dostępna wersja systemu operacyjnego Windows Server w chmurze Azure?
   Odpowiedź: Windows Server 2008 R2 SP1
2. Jakie cechy ma maszyna wirtualna w podstawowej warstwie rozmiarów?
   Odpowiedź: niski wskaźnik IOPS
3. Jakie zastosowania ma maszyna wirtualna o niskim priorytecie?
   Odpowiedź: wsadowe przetwarzanie danych
4. Opcja Rozmiar w widoku maszyny wirtualnej jest wykorzystywana do:
   Odpowiedź: obie powyższe odpowiedzi są poprawne
5. Element Runbook służy do:
   Odpowiedź: obie powyższe odpowiedzi są poprawne
6. Moduł równoważenia obciążenia służy do:
   Odpowiedź: rozdzielania obciążenia pomiędzy maszyny wirtualne umieszczone w puli zaplecza
7. Efektem umieszczenia maszyn wirtualnych w tym samym zestawie dostępności jest:
   Odpowiedź: tworzenie maszyn w różnych szafach
8. Rozbudowa infrastruktury poprzez tworzenie dodatkowych maszyn wirtualnych nosi nazwę:
   Odpowiedź: powiększania
9. Powiększanie zestawu maszyn wirtualnych nosi nazwę:
   Odpowiedź: skalowania w poziomie
10. Do skalowania infrastruktury wykorzystuje się:
    Odpowiedź: zestaw skalowania

## Rozdział 4. Azure App Service — udostępnianie aplikacji internetowych bez serwera

1. Usługa aplikacji w chmurze Azure to przykład modelu:
   Odpowiedź: PaaS
2. Jaką kontrolę nad aplikacją ma użytkownik w planie usługi aplikacji w porównaniu z wirtualną maszyną?
   Odpowiedź: mniejszą
3. Jaki jest nakład pracy administracyjnej w planie usługi aplikacji w porównaniu z wirtualną maszyną?
   Odpowiedź: mniejszy
4. Plan usługi aplikacji stosuje się do udostępniania:
   Odpowiedź: aplikacji internetowych
5. Miejsca wdrożenia aplikacji służą do:
   Odpowiedź: udostępniania różnych wersji aplikacji
6. Wzrosty obciążenia obsługuje się w planie usługi aplikacji poprzez:
   Odpowiedź: skalowanie aplikacji w poziomie
7. Najlepszym narzędziem do monitorowania aplikacji internetowej w chmurze Azure jest:
   Odpowiedź: usługa Application Insights
8. Wysoką dostępność aplikacji internetowej uzyskuje się poprzez:
   Odpowiedź: utworzenie menedżera ruchu
9. Menedżer ruchu obsługuje:
   Odpowiedź: obie powyższe odpowiedzi są poprawne
10. Dedykowane, odizolowane środowisko aplikacji internetowej w chmurze Azure to:
    Odpowiedź: środowisko ASE

## Rozdział 5. Platforma danych Azure

1. Bazy danych w chmurze Azure można tworzyć w modelu:
   Odpowiedź: obie powyższe odpowiedzi są poprawne
2. Maszyna wirtualna z serwerem SQL Server różni się od maszyny bez serwera:
   Odpowiedź: konfiguracją
3. Baza Azure SQL Database jest również określania mianem modelu:
   Odpowiedź: Database as a Service
4. Warstwę cenową bazy Azure SQL Database określa:
   Odpowiedź: obie powyższe odpowiedzi są poprawne
5. Zapytania do bazy Azure SQL Database można wysyłać za pomocą:
   Odpowiedź: obie powyższe odpowiedzi są poprawne
6. Aby połączyć się z bazą Azure SQL Database, należy:
   Odpowiedź: utworzyć regułę zapory zawierającą adres IP
7. Aby utworzyć replikę bazy Azure SQL Database, należy:
   Odpowiedź: skonfigurować replikację geograficzną bazy
8. Aby uzyskać wysoką dostępność bazy Azure SQL Database, należy:
   Odpowiedź: utworzyć grupę trybu failover
9. Do maskowania kolumn danych w bazie Azure SQL Database wykorzystuje się:
   Odpowiedź: dynamiczne maskowanie danych
10. Do wykrywania potencjalnych zagrożeń bazy danych stosuje się:
    Odpowiedź: zaawansowaną ochronę przed zagrożeniami

## Rozdział 6. Przenoszenie danych do Azure: magazyn, kopie zapasowe i usługa Site Recovery

1. Aby uzyskać najwyższy wskaźnik SLA, magazyn danych musi być:
   Odpowiedź: geograficznie nadmiarowy
2. Konto magazynu jest dostępne w wersji:
   Odpowiedź: w obu wersjach
3. Czy można w chmurze Azure utworzyć kopię lokalnej bazy danych?
   Odpowiedź: tak
4. Czy można w chmurze Azure wdrożyć bezpośrednio bazę danych?
   Odpowiedź: tak
5. Aby móc korzystać z usługi Site Recovery, należy utworzyć:
   Odpowiedź: konto magazynu
6. Usługę tworzenia kopii zapasowej w chmurze Azure wykorzystuje się do zabezpieczania:
   Odpowiedź: obie powyższe odpowiedzi są poprawne
7. Usługę Site Recovery wykorzystuje się do zabezpieczania:
   Odpowiedź: obie powyższe odpowiedzi są poprawne
8. Aby przenieść maszynę wirtualną do chmury za pomocą usługi Site Recovery, należy:
   Odpowiedź: dokonać przełączenia maszyn
9. W celu przeniesienia do chmury dużej ilość danych można użyć:
   Odpowiedź: zadania importu/eksportu danych

## Rozdział 7. Chmura hybrydowa — rozszerzenie lokalnej infrastruktury na chmurę Azure

1. W niektórych sytuacjach chmura hybrydowa jest jedynym rozwiązaniem ze względu na:
    Odpowiedź: obie powyższe odpowiedzi są poprawne
2. Sieć lokalną z chmurą Azure można łączyć za pomocą:
    Odpowiedź: obie powyższe odpowiedzi są poprawne
3. Do utworzenia połączenia typu lokacja – lokacja potrzebna jest:
    Odpowiedź: brama sieci wirtualnej
4. Brama sieci lokalnej przechowuje konfigurację:
    Odpowiedź: sieci lokalnej
5. Czy z portalu Azure można pobrać konfigurację urządzenia VPN?
    Odpowiedź: tak, ale tylko dla niektórych urządzeń
6. Jaki jest zalecany model wdrożenia połączenia równorzędnego?
    Odpowiedź: Resource Manager
7. Aby móc zarządzać tożsamością użytkowników w chmurze hybrydowej, należy wdrożyć:
    Odpowiedź: kontroler domeny w chmurze Azure
8. Lokalna brama danych może być używana:
    Odpowiedź: z wybranymi usługami Azure
9. Azure Stack to:
    Odpowiedź: rozszerzenie chmury Azure na lokalne centrum danych
10. Azure Stack oferuje modele:
    Odpowiedź: obie powyższe odpowiedzi są poprawne

## Rozdział 8. Azure Active Directory — tożsamość w chmurze

1. Usługa Azure Active Directory znajduje się na szczycie hierarchii:
    Odpowiedź: podmiotu
2. Czy konto użytkownika może należeć do kilku podmiotów?
    Odpowiedź: tak
3. Czy usługę AAD można wykorzystywać wraz z kontami Microsoft Live?
    Odpowiedź: tak
4. Czy usługę AAD można synchronizować z usługą Windows Server AD?
    Odpowiedź: tak
5. W bezpłatnej warstwie usługi AAD można utworzyć:
    Odpowiedź: 500 000 obiektów
6. Aby skonfigurować niestandardową domenę, należy:
    Odpowiedź: podać nazwę posiadanej domeny
7. Do weryfikacji domeny niestandardowej wykorzystuje się:
    Odpowiedź: jeden z powyższych rekordów
8. Mechanizm RBAC można wykorzystywać do przypisywania ról:
    Odpowiedź: wszystkim powyższym
9. Role można przypisywać:
    Odpowiedź: użytkownikom i grupom użytkowników
10. Aby aplikacja mogła uwierzytelniać użytkowników za pomocą usługi AAD, należy:
    Odpowiedź: zarejestrować aplikację w usłudze AAD

## Rozdział 9. Bezpieczeństwo i administracja w chmurze Azure

1. W ilu kopiach przechowywane są dane w chmurze Azure?
    Odpowiedź: w trzech
2. Większość włamań do zasobów jest efektem:
    Odpowiedź: wycieku poświadczeń
3. Skrót MFA oznacza:
    Odpowiedź: uwierzytelnienie wieloskładnikowe
4. W procesie MFA wykorzystuje się:
    Odpowiedź: wszystkie powyższe
5. Zapora Azure to przykład modelu:
    Odpowiedź: FaaS
6. Zasoby w chmurze Azure mogą być szyfrowane za pomocą:
    Odpowiedź: obie powyższe odpowiedzi są poprawne
7. Aby korzystać z własnych kluczy, należy użyć:
    Odpowiedź: magazynu kluczy
8. Przeznaczeniem centrum zabezpieczeń Azure jest:
    Odpowiedź: obie powyższe odpowiedzi są poprawne
9. Za pomocą centrum zabezpieczeń Azure może chronić zasoby:
    Odpowiedź: obie powyższe odpowiedzi są poprawne
10. Dostęp just in time zapewnia:
    Odpowiedź: kontrolę nad użytkownikami korzystającymi z maszyn wirtualnych

## Rozdział 10. Dobre praktyki

1. Nazwa zasobu powinna zawierać:
    Odpowiedź: jak najwięcej informacji
2. Publiczne punkty końcowe powinny być:
    Odpowiedź: udostępniane w Internecie tylko w razie potrzeby
3. Do kontrolowania dostępu administracyjnego do maszyn wirtualnych służy:
    Odpowiedź: obie powyższe odpowiedzi są poprawne
4. Uwierzytelnienie wieloskładnikowe jest usługą:
    Odpowiedź: bezpłatną dla administratorów
5. Akronim IaC oznacza:
    Odpowiedź: Infrastructure as Code (infrastruktura jako kod)
6. Szablon ARM to:
    Odpowiedź: plik w formacie JSON
7. W wierszu poleceń można korzystać z:
    Odpowiedź: obie powyższe odpowiedzi są poprawne
8. Za pomocą modelu IaC można:
    Odpowiedź: wdrażać wiele zasobów
9. Akronim DSC oznacza:
    Odpowiedź: Desired State Configuration (konfiguracja pożądanego stanu)
10. Automatyzacja za pomocą platformy DSC składa się z następujących etapów:
    Odpowiedź: import skryptu, kompilacja skryptu, rejestracja węzła
