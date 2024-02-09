# Задание 1
Система представляет собой многозадачный компьютер,
в котором запущены на выполнение процессы со следующим профилем нагрузки: 
(вычисления обозначаются как CPU (время в мс), ввод-вывод как IO (время в мс) 

Процесс 1: `CPU(6);IO1(14);CPU(6);IO1(18);CPU(6);IO2(14);CPU(2);IO1(16);CPU(10);IO2(16);CPU(4);IO2(14);`

Процесс 2: `CPU(8);IO1(12);CPU(6);IO2(12);CPU(8);IO2(20);CPU(2);IO2(12);`

Процесс 3: `CPU(4);IO1(12);CPU(6);IO1(14);CPU(2);IO2(10);CPU(8);IO2(18);CPU(4);IO1(14);`

Процесс 4: `CPU(24);IO2(14);CPU(36);IO2(18);CPU(60);IO2(14);CPU(48);IO2(16);CPU(12);IO1(18);`

Процесс 5: `CPU(6);IO1(12);CPU(2);IO2(18);CPU(10);IO2(10);CPU(2);IO2(12);CPU(10);IO1(16);CPU(8);IO1(12);`

Процесс 6: `CPU(10);IO1(18);CPU(10);IO2(10);CPU(8);IO1(16);CPU(2);IO1(20);`

Общесистемные параметры:
- количество процессоров в системе - 4;
- в начальный момент времени в систему добавлены процессы, в количестве - 6.
  При этом процесс 1 был добавлен первым, спустя 2 мс был добавлен процесс 2, спустя 2 мс процесс 3, и т.д.;
- в системе присутствуют два устроайства ввода вывода (IO1,IO2), каждое из которых имеет свою FCFS очередь;
- алгоритмы планирования - FCFS, RR c квантом времени 1 мс, RR с квантом времени в 4 мс, SPN, SRT, HRRN.
  (см. Столлингс, гл. 9.2)
  
Проведите анализ исполнения процессов в алгоритмах планирования ответив, как минимум, на следующие вопросы:
- какой алгоритм планирования обеспечивает обеспечивает самое быстрое выполнение процесса с номером N?;
- как влияют алгоритмы планирования на характеристики исполнения процессов?;
- cколько времени потратит система до завершения всех процессов?;
- к чему в пределе стремится каждый алгоритм планирования?;
- как ведут себя короткие процессы по сравнению с длинными процессами?;
- другие вопросы преподавателя;
  
# Задание 2. 
Программа работает в операционной системе, которая осуществляет замещение кадров
основной памяти страницами во вторичной памяти. При обращении к странице, которая отсутствует
в основной памяти, происходит замещение страницы по заданному алгоритму.

`Количество кадров в основной памяти, выделенных программе, равно 5.`

Кадры в основной памяти в начале работы программы не инициализированны.
Количество страниц в виртуальной памяти процесса равно 24.
Программа осуществляет обращения к страницам в следующем порядке:

`[8, 20, 11, 21, 8, 6, 9, 15, 3, 14, 2, 20, 17, 9, 12, 18, 7, 13, 16, 21, 16, 15, 10, 14, 3, 
23, 5, 24, 16, 9, 3, 2, 12, 24, 18]`

Рассмотреть стратегии замещения - Оптимальную, LRU, FIFO (Столлингс, гл.8.2). 

Для каждого алгоритма:
- нарисовать состояние кадров основной памяти во время обращения программы;
- определить количество операций по замене страниц;
- сравнить количество замен по сравнению с оптимальным.
Как изменится количество замен страниц, если увеличить количество кадров в 2 раза?
А если уменьшить количество кадров в 2 раза?
Сколько должно кадров в памяти, чтобы оптимальный алгоритм давал 5% страничных сбоев?
