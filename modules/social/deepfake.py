import os
import shutil
import subprocess
import json


class DeepfakeFramework:
    TOOLS = {
        "faceswap": {
            "name": "FaceSwap",
            "repo": "https://github.com/deepfakes/faceswap",
            "install": "pip install faceswap",
            "type": "image_video",
            "description": "Swap faces in images and videos using deep learning",
        },
        "wav2lip": {
            "name": "Wav2Lip",
            "repo": "https://github.com/Rudrabha/Wav2Lip",
            "install": "pip install wav2lip",
            "type": "audio_video",
            "description": "Lip-sync generated audio to video in real-time",
        },
        "deepfacelab": {
            "name": "DeepFaceLab",
            "repo": "https://github.com/iperov/DeepFaceLab",
            "install": "Manual installation (Windows GUI)",
            "type": "image_video",
            "description": "Professional-grade face swapping with extensive tooling",
        },
        "so-vits-svc": {
            "name": "So-VITS-SVC",
            "repo": "https://github.com/svc-develop-team/so-vits-svc",
            "install": "pip install so-vits-svc",
            "type": "audio",
            "description": "Singing voice conversion with high naturalness",
        },
        "tortoise_tts": {
            "name": "Tortoise TTS",
            "repo": "https://github.com/neonbjb/tortoise-tts",
            "install": "pip install tortoise-tts",
            "type": "audio",
            "description": "High-quality multi-voice text-to-speech with cloning",
        },
        "stylegan3": {
            "name": "StyleGAN3",
            "repo": "https://github.com/NVlabs/stylegan3",
            "install": "pip install stylegan3",
            "type": "image",
            "description": "Generate high-quality synthetic face images",
        },
        "first_order_model": {
            "name": "First Order Motion Model",
            "repo": "https://github.com/AliaksandrSiarohin/first-order-model",
            "install": "pip install first-order-model",
            "type": "video",
            "description": "Animate still images using driving video motion",
        },
        "roop": {
            "name": "Roop",
            "repo": "https://github.com/s0md3v/roop",
            "install": "pip install roop",
            "type": "image_video",
            "description": "One-click face swapping with no dataset required",
        },
        "voice_cloner": {
            "name": "Voice-Cloner",
            "repo": "https://github.com/voice-cloner/voice-cloner",
            "install": "pip install voice-cloner",
            "type": "audio",
            "description": "Real-time voice cloning from short audio samples",
        },
    }

    def __init__(self):
        self.installed = {}
        self._check_installed()

    def _check_installed(self):
        for tool_name, info in self.TOOLS.items():
            try:
                if tool_name == "roop":
                    import roop
                    self.installed[tool_name] = True
                elif tool_name in ("faceswap", "wav2lip", "so-vits-svc", "voice_cloner"):
                    result = subprocess.run(["python", "-m", tool_name, "--help"],
                                            capture_output=True, text=True, timeout=5)
                    self.installed[tool_name] = result.returncode == 0
                else:
                    self.installed[tool_name] = shutil.which(tool_name) is not None
            except (ImportError, FileNotFoundError, subprocess.TimeoutExpired):
                self.installed[tool_name] = False

    def status(self):
        lines = ["## Deepfake Framework Status", ""]
        lines.append("| Tool | Type | Installed | Description |")
        lines.append("|------|------|-----------|-------------|")
        for name, info in self.TOOLS.items():
            status_icon = "✓" if self.installed.get(name) else "✗"
            lines.append(f"| {info['name']} | {info['type']} | {status_icon} | {info['description']} |")
        lines.append("")
        installed_count = sum(1 for v in self.installed.values() if v)
        lines.append(f"**{installed_count}/{len(self.TOOLS)} tools available**")
        return "\n".join(lines)

    def generate_script(self, tool, action, source=None, target=None, output=None):
        tool_info = self.TOOLS.get(tool)
        if not tool_info:
            return f"# Unknown tool: {tool}. Available: {', '.join(self.TOOLS.keys())}"

        if tool == "faceswap":
            return self._script_faceswap(action, source, target, output)
        elif tool == "wav2lip":
            return self._script_wav2lip(action, source, target, output)
        elif tool == "deepfacelab":
            return self._script_deepfacelab(action, source, target)
        elif tool == "tortoise_tts":
            return self._script_tortoise(action, source, output)
        elif tool == "stylegan3":
            return self._script_stylegan(action, output)
        elif tool == "roop":
            return self._script_roop(action, source, target, output)
        elif tool == "first_order_model":
            return self._script_fom(action, source, target, output)
        elif tool == "so-vits-svc":
            return self._script_sovits(action, source, output)
        elif tool == "voice_cloner":
            return self._script_voice_cloner(action, source, output)
        return f"# Tool {tool} — no script template available"

    def _script_faceswap(self, action, source, target, output):
        if action == "extract":
            return f"""# Extract faces from source video
faceswap extract -i {source or 'input_video.mp4'} -o {output or 'faces_output/'} -D s3fd -A fan"""
        elif action == "train":
            return f"""# Train model on extracted faces
faceswap train -A {source or 'faces_a/'} -B {target or 'faces_b/'} -m {output or 'models/'} -t lightweight"""
        elif action == "convert":
            return f"""# Convert source video with trained model
faceswap convert -i {source or 'input_video.mp4'} -o {output or 'output_video.mp4'} -m {target or 'models/'}"""
        elif action == "single":
            return f"""# Single face swap on image
faceswap convert -i {source or 'input.jpg'} -o {output or 'output.jpg'} -m {target or 'models/'} -s 0"""
        return "# Unknown faceswap action. Use: extract, train, convert, single"

    def _script_wav2lip(self, action, source, target, output):
        if action == "sync":
            return f"""# Lip-sync video with audio
python Wav2Lip/inference.py --checkpoint_path Wav2Lip/checkpoints/wav2lip_gan.pth \\
    --face {source or 'input_video.mp4'} \\
    --audio {target or 'input_audio.wav'} \\
    --outfile {output or 'synced_video.mp4'}"""
        elif action == "enhanced":
            return f"""# Lip-sync with enhanced model
python Wav2Lip/inference.py --checkpoint_path Wav2Lip/checkpoints/wav2lip_gan.pth \\
    --face {source or 'input_video.mp4'} \\
    --audio {target or 'input_audio.wav'} \\
    --outfile {output or 'synced_video.mp4'} \\
    --resize_factor 2 --pads 0 10 0 0"""
        return "# Unknown wav2lip action. Use: sync, enhanced"

    def _script_deepfacelab(self, action, source, target):
        if action == "workspace":
            return """# DeepFaceLab workspace setup
1. Download DeepFaceLab from https://github.com/iperov/DeepFaceLab
2. Extract to C:\\DeepFaceLab
3. Copy source video to workspace\\data_src\\video.mp4
4. Copy target video to workspace\\data_dst\\video.mp4
5. Run 2_extract_images_from_data_src.bat
6. Run 3_extract_images_from_data_dst.bat
7. Run 4_extract_faces.bat
8. Run 5_train_model.bat (SAEHD model recommended)
9. Run 6_convert_model.bat"""
        return "# DeepFaceLab actions: workspace"

    def _script_tortoise(self, action, source, output):
        if action == "clone_voice":
            return f"""# Clone voice from audio sample
python -c "
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio
tts = TextToSpeech()
voice_samples = [load_audio('{source or 'voice_sample.wav'}', 22050)]
text = 'Your generated speech text here'
audio = tts.tts(text, voice_samples=voice_samples)
import torch
torch.save(audio, '{output or 'cloned_voice.pt'}')
" """
        elif action == "generate":
            return f"""# Generate speech with cloned voice
python -c "
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio
tts = TextToSpeech()
voice_samples = [load_audio('{source or 'voice_sample.wav'}', 22050)]
text = 'The target will hear this message and believe it is from a trusted contact.'
for i, chunk in enumerate(tts.tts_stream(text, voice_samples=voice_samples)):
    chunk.save('{output or 'speech_'}{{i}}.wav')
" """
        return "# Unknown tortoise action. Use: clone_voice, generate"

    def _script_stylegan(self, action, output):
        if action == "generate":
            return f"""# Generate synthetic face images
python -c "
import torch
sys.path.append('stylegan3')
from stylegan3.generate import generate_images
network_pkl = 'https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhq-1024x1024.pkl'
generate_images(network_pkl=network_pkl, seeds=[{','.join(str(i) for i in range(10))}], truncation_psi=0.7, outdir='{output or 'generated_faces/'}')
" """
        return "# Unknown stylegan action. Use: generate"

    def _script_roop(self, action, source, target, output):
        if action == "swap":
            return f"""# Swap face in image
roop -s {source or 'source_face.jpg'} -t {target or 'target_image.jpg'} -o {output or 'swapped.jpg'}"""
        elif action == "video":
            return f"""# Swap face in video
roop -s {source or 'source_face.jpg'} -t {target or 'target_video.mp4'} -o {output or 'swapped_video.mp4'} --execution-provider cuda --frame-processor face_swapper"""
        elif action == "many":
            return f"""# Batch face swap in directory
roop -s {source or 'source_face.jpg'} -t {target or 'target_dir/'} -o {output or 'output_dir/'} --batch"""
        return "# Unknown roop action. Use: swap, video, many"

    def _script_fom(self, action, source, target, output):
        if action == "animate":
            return f"""# Animate still image with driving video
python demo.py --checkpoint first-order-model/checkpoints/vox.pth.tar \\
    --source_image {source or 'source_face.jpg'} \\
    --driving_video {target or 'driving_video.mp4'} \\
    --result_video {output or 'animated.mp4'} --relative --adapt_scale"""
        return "# Unknown fom action. Use: animate"

    def _script_sovits(self, action, source, output):
        if action == "convert":
            return f"""# Convert voice using So-VITS-SVC
# 1. Prepare dataset of target voice (10-60min clean audio)
# 2. Preprocess:
python preprocess.py -c configs/config.json
# 3. Train:
python train.py -c configs/config.json -m {output or 'logs/voice_model/'}
# 4. Infer:
python main.py -i {source or 'input_audio.wav'} -m {output or 'logs/voice_model/'} -o {output or 'converted.wav'}"""
        return "# Unknown sovits action. Use: convert"

    def _script_voice_cloner(self, action, source, output):
        if action == "clone":
            return f"""# Clone voice from sample
voice-cloner --input {source or 'voice_sample.wav'} --output {output or 'cloned_model.pth'} --name target_voice"""
        elif action == "speak":
            return f"""# Generate speech from cloned voice
voice-cloner --model {source or 'cloned_model.pth'} --text "Your generated message here" --output {output or 'output.wav'}"""
        return "# Unknown voice_cloner action. Use: clone, speak"

    def pipeline_phishing_call(self, target_voice_sample, script_text, output_video="deepfake_call.mp4"):
        return f"""# Deepfake Voice Phishing Pipeline
# Step 1: Clone voice
voice-cloner --input {target_voice_sample} --output cloned_model.pth --name target

# Step 2: Generate speech from script
voice-cloner --model cloned_model.pth --text "{script_text}" --output generated_audio.wav

# Step 3: Optionally sync with video of target (if source video available)
# python Wav2Lip/inference.py --face target_video.mp4 --audio generated_audio.wav --outfile {output_video}

echo "Pipeline complete. generated_audio.wav ready for vishing campaign."
"""

    def pipeline_deepfake_video(self, source_face, driving_video, target_audio=None):
        parts = [f"# Deepfake Video Pipeline",
                 f"# Step 1: Extract face from source",
                 f"python -c \"import cv2; img=cv2.imread('{source_face}'); print('Face extracted')\"",
                 f"",
                 f"# Step 2: Animate with driving video (First Order Motion)",
                 f"python demo.py --checkpoint fom/checkpoints/vox.pth.tar --source_image {source_face} --driving_video {driving_video} --result_video animated_face.mp4 --relative --adapt_scale"]
        if target_audio:
            parts.extend([
                f"",
                f"# Step 3: Lip-sync with target audio (Wav2Lip)",
                f"python Wav2Lip/inference.py --face animated_face.mp4 --audio {target_audio} --outfile final_deepfake.mp4",
            ])
        else:
            parts.append(f"\n# Step 3: (optional) Add Wav2Lip sync with audio")
        return "\n".join(parts)

    def generate_persona_images(self, count=5, output_dir="generated_personas"):
        return f"""# Generate synthetic persona faces using StyleGAN3
python -c "
import sys; sys.path.append('stylegan3')
from stylegan3.generate import generate_images
generate_images(
    network_pkl='https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhq-1024x1024.pkl',
    seeds=[{','.join(str(i) for i in range(count))}],
    truncation_psi=0.7,
    outdir='{output_dir}'
)
print('Generated {count} persona faces in {output_dir}')
" """

    def get_available_tools(self):
        return [
            {"name": name, **info, "installed": self.installed.get(name, False)}
            for name, info in self.TOOLS.items()
        ]

    def generate_report(self, include_install_guide=True):
        lines = ["# Deepfake Framework Guide", ""]
        lines.append("## Overview")
        lines.append("This framework orchestrates external deepfake generation tools.")
        lines.append("No tools are bundled — each must be installed separately.")
        lines.append("")
        lines.append("## Available Tools")
        for name, info in self.TOOLS.items():
            installed = "✓" if self.installed.get(name) else "✗"
            lines.append(f"### {info['name']} [{installed}]")
            lines.append(f"- Type: {info['type']}")
            lines.append(f"- Install: `{info['install']}`")
            lines.append(f"- Repo: {info['repo']}")
            lines.append(f"- {info['description']}")
            lines.append("")
        if include_install_guide:
            lines.append("## Quick Install")
            lines.append("```bash")
            lines.append("pip install faceswap wav2lip tortoise-tts stylegan3")
            lines.append("git clone https://github.com/s0md3v/roop && cd roop && pip install -r requirements.txt")
            lines.append("```")
        return "\n".join(lines)
