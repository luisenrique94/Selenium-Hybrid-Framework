pytest -s -v -m "sanity" --html=./Reports/prueba.html testCases/ --browser chrome
rem pytest -s -v -m "sanity" --html=./Reports/prueba.html testCases/ --browser firefox
rem pytest -s -v -m "sanity or regression" --html=./Reports/prueba.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/prueba.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/prueba.html testCases/ --browser chrome

