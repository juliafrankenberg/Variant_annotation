from flask import Flask, request, jsonify, render_template
import subprocess
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_workflow', methods=['POST'])
def run_workflow():
    try:
        subprocess.run(['snakemake', '--cores', '1'], check=True)
        return jsonify({"status": "success", "message": "Workflow executed successfully."})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/get_vcf', methods=['GET'])
def get_vcf():
    vcf_file_path = "results/annotated_variants.vcf"  # Make sure to use the correct VCF file

    try:
        df = pd.read_csv(vcf_file_path, sep='\t', comment='#', header=None)
        df.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'SAMPLE']
        
        # Extract DP and Gene Name
        df['DP'] = df['INFO'].str.extract(r'DP=(\d+)')[0].astype(float)
        df['Gene'] = df['INFO'].str.extract(r'ANN=[^|]*\|[^|]*\|[^|]*\|([^|]*)')[0]

        # Get the minimum DP filter value from the query parameters
        min_dp = request.args.get('min_dp', type=float)

        # Filter the DataFrame based on DP value if specified
        if min_dp is not None:
            df = df[df['DP'] >= min_dp]

        # Select only the relevant columns
        df = df[['Gene', 'DP', 'CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER']]
        
        # Convert DataFrame to a list of dictionaries
        vcf_data = df.to_dict(orient='records')
    
        # Check for a query parameter to return JSON
        if request.args.get('format') == 'json':
            return jsonify(vcf_data)

        return render_template('vcf_data.html', vcf_data=vcf_data)

    except FileNotFoundError:
        print("File not found:", vcf_file_path)  # Log the file path
        return jsonify({"error": "VCF file not found."}), 404
    except Exception as e:
        print("Error processing VCF data:", str(e))  # Log the error for debugging
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
