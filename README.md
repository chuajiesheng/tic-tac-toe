# Python Tic-Tac-Toe Game

## Design

```                      
   ┌────────────┐        ┌────────────┐          ┌────────────┐
   │            │        │            │          │            │
   │    Main    │───────▶│  GamePlay  │─────────▶│   State    │
   │            │        │            │          │            │
   └────────────┘        └────────────┘          └────────────┘
                                │                              
                                │                              
                                ▼                              
                         ┌────────────┐                        
                         │            │                        
                         │   Board    │                        
                         │            │                        
                         └────────────┘                        
```
1. `Main` handles the input and output and call `GamePlay` for thing to print.
2. `GamePlay` holds the `State` and the `Board`. It mainly process the input and generate the output.
3. `State` just say what the game should be doing now.
4. `Board` say how big it is, whether a cell should be `x` or `o` and check wins or draw.


## Run

```
python game/main.py <size_of_grid>
```

- `size_of_grid` is optional. Default to 3.
- No max size check is done on `size_of_grid`, as long it is a number.


## Test

Only require py.test for testing.

```
pip install -r requirements.txt
make test
```