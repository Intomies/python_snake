# Notes for teacher

### Console command history:

  93  git init
  
  94  echo "# python_snake" >> README.md
  
  95  git add README.md
  
  96  cat README.md
  
  97  git commit -m "First commit"
  
  98  git status
  
  99  git remote add origin https://github.com/Intomies/python_snake.git
  
  100  git push -u origin master
  
  101  history
  
  102  git log --oneline

  242  git status
  
  243  echo /topic >> .gitignore
  
  244  git status
  
  245  git add .gitignore
  
  246  git commit -m "added .gitignore for project"
  
  247  git push -u origin master
  
  248  git status
  
  249  git add game/
  
  250  git status
  
  251  git commit -m "added game-folder, which contains snake_main, the main method of the game and snake_functions, the functions used by                     the game"
  
  257  git push
  
  258  git log --oneline
  
  259  history
  
  260  git status
  
  261  git add notes/NOTES.md
  
  262  git status
  
  263  git commit -m "added new commits to NOTES.md"
  
  264  git push
  
  265  git status
  
  266  history

  267  mkdir 1
  
  268  cd 1
  
  273  curl -OL https://github.com/Intomies/python_snake/archive/1.0.zip
  
  274  dir
  
  276  cd ..
  
  277  echo /1 >> .gitignore
  
  278  cat .gitignore
  
  279  git status
  
  280  history
  
  281  git status
  
  282  git add .gitignore
  
  283  git status
  
  284  git commit -m "added the version 1 folder to .gitignore"
  
  285  git add notes/NOTES.md
  
  286  git commit -m "added the recent commits to notes.md"
  
  287  git push -u origin master
  
  288  git status
  
  290  git log --oneline
  
  291  history
  
  292  git pull
  
  293  git checkout feature
  
  294  git status
  
  295  git add notes/NOTES.md
  
  296  git commit -m "added latest git activities to notes.md"
  
  297  git push -u origin master
  
  298  git pull
  
  299  git checkout feature
  
  300  git status
  
  301  git status
  
  302  git add game/snake_main.py
  
  303  git status
  
  304  git commit -m "added game over-screen to python_main"
  
  305  git push -u origin feature
  
  306  git status
  
  307  git add game/snake_functions.py
  
  308  git commit -m "cleaned the file a little"
  
  309  git status
  
  310  git push -u origin feature
  
  311  git log --oneline
  
  312  git checkout master
  
  313  git add notes/NOTES.md
  
  314  git commit -m "rearranged git activity-tab"
  
  315  git push
  
  316  history


  436  git status
  
  437  cd game
  
  438  git add snake_functions.py
  
  439  git add snake_main.py
  
  440  cd ..
  
  441  git status
  
  442  git status
  
  443  git add .gitignore
  
  444  git commit -m "Added new features, highscore and hitbox for food. Also added __pycache__ to .gitignore"
  
  445  git push
  
  446  git status
  
  447  git checkout master
  
  448  history
  
 #### I dont't know what happened here, but a big paart of my command history has vanished. Luckily the merge, merge conflict and commits can be seen in git log--

  436  git status
  
  437  git add game/snake_main.py
  
  438  git commit -m "minor fixes and commenting"
  
  439  git push
  
  440  git status
  
  441  git checkout feature
  
  442  git status
  
  443  git checkout master
  
  444  git merge feature
  
  445  git commit -m "merged feature branch"
  
  446  history
  
  447  git merge feature
  
  448  git checkout master
  
  449  git checkout feature
  
  450  git checkout master
  
  451  git push -u origin master
  
  452  git checkout master
  
  453  git checkout feature
  
  454  git status
  
  455  git add hs.txt
  
  456  git reset
  
  457  git add game/hs.txt
  
  458  git commit -m "added the highscore-file"
  
  459  git push
  
  460  git checkout master
  
  461  git status
  
  462  git merge feature
  
  463  git push -u origin master
  
  464  git log --onelaine
  
  465  git log --oneline
  
  466  git status
  
  467  git add game/snake_functions.py
  
  468  git add game/snake_main.py
  
  469  git commit -m "minor fixes"
  
  470  git push -u origin master
  
  471  git log --oneline
  
  472  history
  
  479  curl -OL https://github.com/Intomies/python_snake/archive/3.zip
  
  480  git status
  
  481  git status
  
  482  git pull
  
  483  git status
  
  484  git add snake.py
  
  485  git add hs.txt
  
  486  git add .gitignore
  
  487  git add game
  
  488  git status
  
  489  git status
  
  490  git commit -m "Huge commit. Decided to move the whole game into one file, and reworked a lot of stuff to be more OOP. Added a class for game texts and moved almost all functions to be class specific. Also styled the game a little and commented all code."
  
  491  history

### Git activity from latest to oldest:

  (HEAD -> master, origin/master) Huge commit. Decided to move the whole game into one file, and reworked       a lot of stuff to be more OOP. Added a class for game texts and moved almost all functions to be class specific. Also styled the game a little and commented all code.

  (HEAD -> master, origin/master) minor fixes
  
  Merge branch 'feature'
  
  (origin/feature, feature) added the highscore-file
  
  Merge branch 'feature' Because it is importat
  
  minor fixes and commenting
  
  Fixed some bugs
  
  Added starting screen and moved play screen to own loop. Also cleaned up a bit.
  
  added .vscode folder to .gitignore
  
  (HEAD -> master, origin/master) added the version folder /2 in .gitignore
  
  merging feature-branch, merge conflict in gitignore
  
  (HEAD -> feature, origin/feature) Added highscore feature and fixed the snake color not changing bug
  
  (HEAD -> feature, origin/feature) Added new features, highscore and hitbox for food. Also added __pycache__ to .gitignore
  
  (HEAD -> feature, origin/feature) cleaned the file a little
  
  added game over-screen to python_main
  
  (origin/feature, feature) Added highscore feature and fixed the snake color not changing bug
  
  (HEAD -> master, origin/master) added notes to .gitignore and deleted it. Will put them back once the game is finished
  
  (HEAD -> master, origin/master) added latest git activities to notes.md
  
  (HEAD -> master, origin/master) added the recent commits to notes.md
  
  added the version 1 folder to .gitignore
  
  (HEAD -> master) added game-folder, which contains snake_main, the main method of the game and snake_functions, the functions used by the game
  
  (origin/master) added .gitignore for project
  
  added notes.md for teacher
  
  Revert "added history.txt, which contains notes for teacher."
  
  added history.txt, which contains notes for teacher.
  
  (origin/master) First commit
  
  





