import os
import subprocess
import tempfile
import shutil
from gooey import Gooey, GooeyParser

@Gooey(program_name="Audio Separation using Demucs")
def main():
    parser = GooeyParser(description="Separate audio sources using Demucs")

    parser.add_argument('input_file', widget="FileChooser", help="Input audio file (wav,mp3)")
    parser.add_argument('--output_dir', default=None, widget="DirChooser", help="Output directory")
    
    args = parser.parse_args()

    input_file = args.input_file
    output_dir = args.output_dir or os.path.join(os.path.dirname(input_file), 'separated_audio')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Temporary directory for Demucs output
    temp_dir = tempfile.mkdtemp()

    # Run Demucs separation
    subprocess.run(['demucs.separate', input_file, '--out', temp_dir])

    # Move separated tracks to output directory
    for file in os.listdir(temp_dir):
        if file.endswith('.wav'):
            shutil.move(os.path.join(temp_dir, file), os.path.join(output_dir, file))

    print("Separation completed. Separated tracks are saved in:", output_dir)

    # Clean up temporary directory
    shutil.rmtree(temp_dir)

if __name__ == '__main__':
    main()
