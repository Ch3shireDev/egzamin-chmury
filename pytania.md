# Pytania

## Rozdział 1. Chmura obliczeniowa — podstawowe pojęcia

1. Jakiego rodzaju chmura wymaga posiadania łącza internetowego i pozwala każdemu użytkownikowi korzystać z jej usług?
   a) prywatna
   b) hostowana
   c) publiczna
2. Jaki model usług daje największą kontrolę nad zasobami?
   a) IaaS
   b) PaaS
   c) SaaS
3. W jakim modelu usług zarządzanie infrastrukturą jest najprostsze?
   a) IaaS
   b) PaaS
   c) SaaS
4. Jaki model usług oferuje najnowsze funkcjonalności i aktualizacje?
   a) IaaS
   b) PaaS
   c) SaaS
5. Co decyduje o izolowaniu środowisk klientów w chmurze Azure?
   a) usługa Azure Fabric
   b) podmiot
   c) subskrypcja
6. Jak nazywa się pierwszy poziom dostępu w chmurze Microsoft Azure?
   a) usługa Azure Fabric
   b) podmiot
   c) subskrypcja
7. Jaki jest najniższy poziom szczegółowości dostępu do zasobów?
   a) zasób
   b) grupa zasobów
   c) subskrypcja
8. Jaki jest zalecany poziom szczegółowości dostępu do zasobów Azure?
   a) zasób
   b) grupa zasobów
   c) subskrypcja
9. Jaki jest system naliczania opłat w chmurze Azure?
   a) roczny
   b) miesięczny
   c) minutowy
10. Częścią jakiego modelu są szablony ARM?
    a) IaC
    b) IaaS
    c) konfiguracja jako kod

## Rozdział 2. Sieci — podstawa modelu IaaS

1. Jaki model usług wykorzystuje sieć Azure?
   a) IaaS
   b) PaaS
   c) obie powyższe odpowiedzi są poprawne
2. Co definiuje zakres adresów IP?
   a) maska podsieci
   b) CIDR
   c) RIP
3. Jakie usługi są dołączane do sieci wirtualnej za pomocą punktów końcowych?
   a) maszyny wirtualne
   b) PaaS
   c) SaaS
4. Domyślnym serwerem DNS w chmurze Azure jest:
   a) serwer Azure DNS
   b) publiczny serwer DNS
   c) niestandardowy serwer DNS
5. Kiedy można tworzyć punkty usług?
   a) podczas tworzenia sieci wirtualnej
   b) po utworzeniu sieci wirtualnej
   c) w dowolnym momencie
6. Prywatny adres IP w sieci Azure jest:
   a) dynamiczny
   b) statyczny
   c) dynamiczny lub statyczny
7. Publiczny adres IP w sieci Azure jest:
   a) dynamiczny
   b) statyczny
   c) dynamiczny lub statyczny
8. Sieciowa grupa zabezpieczeń to:
   a) zbiór reguł bezpieczeństwa kontrolujących przepływ ruchu
   b) reguły rezerwacji adresów IP
   c) obie powyższe odpowiedzi są poprawne
9. Co definiuje sieciowa grupa zabezpieczeń?
   a) reguły zabezpieczeń dla ruchu przychodzącego
   b) reguły zabezpieczeń dla ruchu wychodzącego
   c) obie powyższe odpowiedzi są poprawne
10. Do jakiego zasobu można przypisać sieciową grupę zabezpieczeń?
    a) sieci wirtualnej
    b) interfejsu sieciowego
    c) podsieci

## Rozdział 3. Infrastruktura jako usługa — pierwsza warstwa chmury obliczeniowej

1. Jaka jest najstarsza dostępna wersja systemu operacyjnego Windows Server w chmurze Azure?
   a) Windows Server 2003
   b) Windows Server 2008 R2 SP1
   c) Windows Server 2012 R2
2. Jakie cechy ma maszyna wirtualna w podstawowej warstwie rozmiarów?
   a) niski wskaźnik IOPS
   b) równoważenie obciążenia
   c) automatyczne skalowanie
3. Jakie zastosowania ma maszyna wirtualna o niskim priorytecie?
   a) usługi o wysokiej dostępności
   b) wsadowe przetwarzanie danych
   c) równoważenie obciążenia
4. Opcja Rozmiar w widoku maszyny wirtualnej jest wykorzystywana do:
   a) skalowania maszyny w górę
   b) skalowania maszyny w dół
   c) oba powyższe
5. Element Runbook służy do:
   a) wykonywania operacji utrzymaniowych
   b) skalowania maszyny wirtualnej w górę i w dół
   c) oba powyższe
6. Moduł równoważenia obciążenia służy do:
   a) rozdzielania obciążenia pomiędzy maszyny wirtualne umieszczone w puli zaplecza
   b) izolowania ruchu sieciowego i zabezpieczania maszyny wirtualnej przez atakami
   c) oba powyższe
7. Efektem umieszczenia maszyn wirtualnych w tym samym zestawie dostępności jest:
   a) tworzenie maszyn w różnych centrach danych Azure
   b) tworzenie maszyn w różnych szafach
   c) tworzenie maszyn w tej samej szafie
8. Rozbudowa infrastruktury poprzez tworzenie dodatkowych maszyn wirtualnych nosi nazwę:
   a) skalowania w górę
   b) skalowania w dół
   c) powiększania
9. Powiększanie zestawu maszyn wirtualnych nosi nazwę:
   a) skalowania w pionie
   b) skalowania w poziomie
   c) skalowania ukośnego
10. Do skalowania infrastruktury wykorzystuje się:
    a) strefę dostępności
    b) zestaw dostępności
    c) zestaw skalowania

## Rozdział 4. Azure App Service — udostępnianie aplikacji internetowych bez serwera

1. Usługa aplikacji w chmurze Azure to przykład modelu:
   a) IaaS
   b) PaaS
   c) SaaS
2. Jaką kontrolę nad aplikacją ma użytkownik w planie usługi aplikacji w porównaniu z wirtualną maszyną?
   a) większą
   b) mniejszą
   c) taką samą
3. Jaki jest nakład pracy administracyjnej w planie usługi aplikacji w porównaniu z wirtualną maszyną?
   a) większy
   b) mniejszy
   c) taki sam
4. Plan usługi aplikacji stosuje się do udostępniania:
   a) aplikacji internetowych
   b) baz danych
   c) obu usług
5. Miejsca wdrożenia aplikacji służą do:
   a) udostępniania różnych wersji aplikacji
   b) udostępniania aplikacji w różnych regionach
   c) obsługiwania zwiększonego obciążenia
6. Wzrosty obciążenia obsługuje się w planie usługi aplikacji poprzez:
   a) skalowanie aplikacji w pionie
   b) skalowanie aplikacji w poziomie
   c) uruchamianie zadań WebJob
7. Najlepszym narzędziem do monitorowania aplikacji internetowej w chmurze Azure jest:
   a) Splunk
   b) analiza dzienników
   c) usługa Application Insights
8. Wysoką dostępność aplikacji internetowej uzyskuje się poprzez:
   a) skalowanie aplikacji w pionie
   b) skalowanie aplikacji w poziomie
   c) utworzenie menedżera ruchu
9. Menedżer ruchu obsługuje:
   a) punkty końcowe Azure
   b) zewnętrzne punkty końcowe
   c) oba rodzaje
10. Dedykowane, odizolowane środowisko aplikacji internetowej w chmurze Azure to:
    a) plan usługi aplikacji
    b) środowisko ASE
    c) maszyna wirtual

## Rozdział 5. Platforma danych Azure

1. Bazy danych w chmurze Azure można tworzyć w modelu:
   a) IaaS
   b) PaaS
   c) w obu
2. Maszyna wirtualna z serwerem SQL Server różni się od maszyny bez serwera:
   a) konfiguracją
   b) wielkością pamięci i liczbą rdzeni procesora
   c) nazwą
3. Baza Azure SQL Database jest również określania mianem modelu:
   a) Database as a Service
   b) SQL as a Service
   c) Data as a Service
4. Warstwę cenową bazy Azure SQL Database określa:
   a) liczba jednostek DTU
   b) liczba wirtualnych rdzeni procesora
   c) oba powyższe
5. Zapytania do bazy Azure SQL Database można wysyłać za pomocą:
   a) programu SQL Server Management Studio
   b) edytora zapytań w portalu Azure
   c) obu narzędzi
6. Aby połączyć się z bazą Azure SQL Database, należy:
   a) utworzyć regułę zapory zawierającą adres IP
   b) wskazać legalny adres IP w ustawieniach sieci wirtualnej
   c) wskazać legalny adres IP w ustawieniach głównej bazy danych
7. Aby utworzyć replikę bazy Azure SQL Database, należy:
   a) utworzyć kopię bazy
   b) wyeksportować bazę
   c) skonfigurować replikację geograficzną bazy
8. Aby uzyskać wysoką dostępność bazy Azure SQL Database, należy:
   a) utworzyć grupę trybu failover
   b) utworzyć klaster trybu failover
   c) użyć opcji Zawsze włączone
9. Do maskowania kolumn danych w bazie Azure SQL Database wykorzystuje się:
   a) przezroczyste szyfrowanie danych
   b) dynamiczne maskowanie danych
   c) klasyfikowanie danych
10. Do wykrywania potencjalnych zagrożeń bazy danych stosuje się:
    a) ocenę luk w zabezpieczeniach
    b) zaawansowaną ochronę przed zagrożeniami
    c) obie funkcjonalności

## Rozdział 7. Chmura hybrydowa — rozszerzenie lokalnej infrastruktury na chmurę Azure

1. W niektórych sytuacjach chmura hybrydowa jest jedynym rozwiązaniem ze względu na:
   a) obowiązujące przepisy
   b) dokonane inwestycje
   c) obie powyższe odpowiedzi są poprawne
2. Sieć lokalną z chmurą Azure można łączyć za pomocą:
   a) połączenia typu lokacja – lokacja
   b) usługi ExpressRoute
   c) obie powyższe odpowiedzi są poprawne
3. Do utworzenia połączenia typu lokacja – lokacja potrzebna jest:
   a) brama sieci wirtualnej
   b) lokalna brama danych
   c) obie powyższe odpowiedzi są poprawne
4. Brama sieci lokalnej przechowuje konfigurację:
   a) sieci wirtualnej
   b) sieci lokalnej
   c) obie powyższe odpowiedzi są poprawne
5. Czy z portalu Azure można pobrać konfigurację urządzenia VPN?
   a) tak
   b) tak, ale tylko dla niektórych urządzeń
   c) nie
6. Jaki jest zalecany model wdrożenia połączenia równorzędnego?
   a) Resource Manager
   b) klasyczny
   c) obie powyższe odpowiedzi są poprawne
7. Aby móc zarządzać tożsamością użytkowników w chmurze hybrydowej, należy wdrożyć:
   a) kontroler domeny w grupie odzyskiwania
   b) kontroler domeny w chmurze Azure
   c) grupę zawsze dostępnych maszyn
8. Lokalna brama danych może być używana:
   a) ze wszystkimi usługami Azure
   b) z wybranymi usługami Azure
   c) z jedną usługą Azure
9. Azure Stack to:
   a) rozszerzenie chmury Azure na lokalne centrum danych
   b) rozszerzenie lokalnego centrum danych na chmurę Azure
   c) rozszerzenie chmury Azure na inną chmurę publiczną
10. Azure Stack oferuje modele:
    a) IaaS
    b) PaaS
    c) obie powyższe odpowiedzi są poprawne

## Rozdział 8. Azure Active Directory — tożsamość w chmurze

1. Usługa Azure Active Directory znajduje się na szczycie hierarchii:
   a) podmiotu
   b) subskrypcji
   c) grupy zasobów
2. Czy konto użytkownika może należeć do kilku podmiotów?
   a) tak
   b) nie
3. Czy usługę AAD można wykorzystywać wraz z kontami Microsoft Live?
   c) tak
   d) nie
4. Czy usługę AAD można synchronizować z usługą Windows Server AD?
   a) tak
   b) nie
5. W bezpłatnej warstwie usługi AAD można utworzyć:
   a) 5000 obiektów
   b) 500 000 obiektów
   c) 5 000 000 obiektów
6. Aby skonfigurować niestandardową domenę, należy:
   a) podać dowolną nazwę domeny
   b) podać nazwę posiadanej domeny
   c) użyć sufiksu onmicrosoft.com
7. Do weryfikacji domeny niestandardowej wykorzystuje się:
   a) rekord MX
   b) rekord TXT
   c) jeden z powyższych
   d) oba powyższe
8. Mechanizm RBAC można wykorzystywać do przypisywania ról:
   a) subskrypcjom
   b) grupom zasobów
   c) zasobom
   d) wszystkim powyższym
9. Role można przypisywać:
   a) użytkownikom
   b) grupom użytkowników
   c) użytkownikom i grupom użytkowników
10. Aby aplikacja mogła uwierzytelniać użytkowników za pomocą usługi AAD, należy:
    a) zarejestrować aplikację w usłudze AAD
    b) utworzyć grupę AAD w aplikacji
    c) wykonać obie operacje
