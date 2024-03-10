## TESTY NA FLP 1. PROJEKT - DECISION TREES

#### ❗ Requirements
* Python 3.11

#### Pouzitie
1. Umiestnite `flp-fun.hs` a `Makefile` do zlozky s `.py` subormi.
2. Spustite `python3 main.py`

#### ⚠️ Disclaimer
* Neda sa celkom definovat prijatelna odchylka od vzoroveho riesenia v druhej casti, kvoli porovnavaniu FP cisel a roznej presnosti v pythone vs haskelli a taktiez kvoli odlisnosti pristupov, resp. vyuzitie inych metod alebo vylepseni.

* Na windows je nutne nastavit ine zalamovanie riadkov, staci vymenit (odkomentovat a zakomentovat) `main.py:36-37`.

* Testuju sa iba nahodne vektory, za doplenenie edge case-ov alebo za PR s opravami chyb budem rad.

* Na konci vystupov nesmie byt newline (nie je to tak v zadani).

* Testy su IBA orientacne.

#### Pouzity sposob kontrukcie stromu
Na vyber dalsieho splitu sa vyuziva vypocet gini impurity a nasledna sa vyberie prvy midpoint s najnizsou impurity.

#### Struktura generovanych testovacich suborob
Skript generuje stvorice suborov trainingdata-tree-newdata-classification.
Na konci kazdeho suboru je newline.

Vygeneruje sa struktura suborov:

* zlozka `./tests/`

  * `training_data/`  so subormi `data_{id}` kde `id` sa inkrementuje s poctom, napr. `data_1`:
    ```
    857.88,230.55,1041.12,498.01,1037.92,654.19,612.74,903.97,1026.55,147.14,Class10
    195.04,630.58,84.49,264.65,679.1,755.53,264.98,1027.58,698.56,436.26,Class4
    455.39,1068.29,587.91,145.0,368.05,247.46,944.34,1023.95,932.45,796.6,Class4
    330.57,749.41,769.63,636.91,197.03,836.98,820.24,440.98,654.48,788.06,Class7
    390.12,877.37,702.6,733.33,927.92,169.15,722.87,475.83,770.99,674.49,Class6
    523.29,280.88,789.01,134.41,358.38,259.73,391.46,457.21,220.92,1105.14,Class6
    444.26,313.48,903.27,380.25,426.05,1162.11,550.87,1067.21,683.33,585.11,Class3
    1137.26,726.15,990.45,99.36,516.06,544.93,618.36,843.65,366.44,217.95,Class10
    363.96,725.92,465.38,454.76,705.19,621.82,899.99,511.56,578.86,295.12,Class1
    460.21,426.03,910.83,836.4,1085.26,991.39,1042.15,584.08,155.16,357.99,Class5
    ```

  * `trees/`  so subormi `tree_{id}` kde `id` sa inkrementuje s poctom, napr. `tree_1`:
    ```
    Node: 0, 690.585
      Node: 2, 645.255
        Node: 3, 359.705
          Leaf: Class4
          Leaf: Class1
        Node: 5, 548.355
          Leaf: Class6
          Node: 0, 387.415
            Leaf: Class7
            Node: 0, 452.235
              Leaf: Class3
              Leaf: Class5
      Leaf: Class10
    ```
  *  `new_data/`  so subormi `new_data_{id}` kde `id` sa inkrementuje s poctom, napr. `new_data_1`:
      ```
      619.73,975.5,1019.12,271.06,261.95,588.47,241.76,251.74,766.54,210.29
      1017.75,77.7,409.8,793.71,834.6,671.88,220.13,575.43,666.97,1057.76
      241.96,771.85,585.63,241.82,732.23,975.01,851.22,944.36,427.55,399.21
      692.64,651.83,214.88,247.96,605.82,894.72,746.27,535.58,1022.9,649.63
      504.62,183.53,475.66,938.32,674.58,515.39,138.47,360.45,694.56,1032.19
      ```
  * `classifications/`  so subormi `classification_{id}` kde `id` sa inkrementuje s poctom, napr. `classification_1`:
    ```
    Class5
    Class10
    Class4
    Class10
    Class1
    ```

#### Priebeh testu

1. Vygenerovanie testcase-ov podla parametrov v `config.py`:
   - `N_TESTS`
   - `FEATURE_SIZE` - velkost generovanych vektorov
   - `N_SAMPLES_TREE` - pocet vektorov, z ktorych sa kontruuje vzorovy strom
   - `NEW_DATA_COUNT` - pocet novych klasifikovanych vektorov
   - `TASK_2_CLASSIFICATIONS` - pocet nahodnych vektorov na otestovanie vzoroveho a skontruovaneho stromu
2. Test prvej casti:
    1. Spustenie `flp-fun` so subormi `tree_ID` a `new_data_ID`
    2. kontrola - program by mal spravne vypisat na vystup triedy (klasifikovane vektory podla zadaneho stromu)
3. Test druhej casti:
    1. Spustenie `flp-fun` so subormi `training_data_ID`
    2. program by mal vypisat na vystup skontruovany strom
    3. Na skontruovanom a vzorovom stroma sa klasifikuje `TASK_2_CLASSIFICATIONS` pocet vektorov. Po porovnani sa vypise pocet odlisnych klasifikacii a percento z celkoveho poctu.
