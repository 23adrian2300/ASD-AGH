# Adrian Żerebiec
# Opis algorytmu: początkowo tablice sortujemy quicksortem. W wyniku tej operacji tablica posortowana jest według dolnych wartości ale gdy mają tą samą wartość dolną to przedziały z większą "górą" są na dalszych pozycjach np.:[[1,6[,[1,8],[2,1]] itd.
# Po posortowaniu przechodzimy do głównej pętli while, w niej pierwsza pętla while działą aby dotrzeć do ostaniego przedziału z tym samym dolnym ograniczeniem ale najwyzeszym górnym, wszytskie poprzednie się w nim zawierają zatem zwiększamy nasz licznik o liczbę tych przedziałów
# Następnie ustawiamy j=i po to aby sprawdzać czy następne przedziały zawierają się w naszym największym dla danego przedziału wybranego w pierwszej pętli while. Zanim przejdziemy do następnego while'a sprawdzamy czy nowy przedział jest sens sprawdzać, czyli czy górne ogranicznie jest większe lub równe poprzednio sprawdzanemu(dla pierwszego przejscia sprawdzamy 0) oraz czy maks ma możliwość być większy od osiągnietego
# Zmieniamy wartośc z_max na j którego teraz sprawdzamy, to wykorszytsamy w drugim przejsciu aby sprawdzic czy jest sens sprawdzac nowy przedział
# Dalej w while'u dodajemy do ilosci zawieranych się przedziałów pzredziały których górny przedział jest większy równy sprawdzanemu i robimy to do momentu w którym nie przekroczymy zakresu i albo maks bedzie miał szanse być większy, później sprawdzamy czy ilo jest większe od maksa, zereujemy ilo, j zwiększamy o jeden aby sprawdzać nowe przedziały z większym dolnym ograniczniem
# i = j aby sprawdzac te nowe przedziały i wykonujemy ponownie algorytmy do momentu w którym maks będzie miał szansę być większy gdyż w przeciwnym razie nie ma sensu sprawdzać
# Złożoność pesymistyczna: n^2 + n^2, średnia nlogn + n


from zad2testy import runtests


def partion(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    while p < r:
        q = partion(A, p, r)
        quicksort(A, p, q - 1)
        p = q + 1
    return A


def depth(L):
    n = len(L)
    quicksort(L, 0, len(L) - 1)
    i, j = 0, 0
    z_max = 0
    maks, ilo = 0, 0
    while i < n - 1:
        while i < n - 1 and L[i][0] == L[i + 1][0]:
            ilo += 1
            i += 1
        j = i
        if L[z_max][1] <= L[j][1] and maks < n - j - 1 + ilo:
            z_max = j
            while ilo + n - i - 1 > maks and i < n - 1:
                if L[j][1] >= L[i + 1][1]:
                    ilo += 1
                i += 1

        if maks < ilo:
            maks = ilo

        ilo = 0
        j += 1
        i = j
        if maks > n - j - 1:
            return maks

    return maks

runtests(depth)
