use std::process::Command;
use std::collections::HashMap;
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct IndexData {
    dates: Vec<String>,
    close: Vec<f64>,
}

fn main() {
    let output = Command::new("python3")
        .arg("get_indices.py")
        .arg("--no-plot")
        .output()
        .expect("Échec de l'exécution du script Python");

    let json_str = String::from_utf8_lossy(&output.stdout);

    // Définir le type de structure attendue
    let parsed: HashMap<String, IndexData> = match serde_json::from_str(&json_str) {
        Ok(p) => p,
        Err(e) => {
            eprintln!("Erreur de parsing JSON : {}", e);
            return;
        }
    };

    for (name, data) in parsed {
        println!("--- {} ---", name);
        for (date, close) in data.dates.iter().zip(data.close.iter()) {
            println!("{} => {}", date, close);
        }
        println!();
    }
}