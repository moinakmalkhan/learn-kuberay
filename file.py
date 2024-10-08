from ray.job_submission import JobSubmissionClient


client = JobSubmissionClient("http://10.42.0.74:8265")

client.submit_job( 
    entrypoint="python script.py",
    runtime_env={
        "working_dir": "./",
        "pip": ["requests==2.26.0"],
        "py_modules": ["https://github.com/moinakmalkhan/learn-kuberay/archive/93f2c48233518db7cc5aefee9ac9c4f8e99b8c38.zip"],
    }
)